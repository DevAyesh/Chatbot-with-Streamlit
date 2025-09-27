from openai import OpenAI
import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.title("DeepSeek AI Chatbot")

# Check if API key is set (works locally and on Streamlit Cloud)
api_key = os.getenv("API_KEY") or st.secrets.get("API_KEY", None)

if not api_key:
    st.error("⚠️ OpenRouter API key not found!")
    st.info("**For Local Development:**")
    st.code("Create .env file with: API_KEY=your-openrouter-api-key")
    st.info("**For Streamlit Cloud:**")
    st.code("Add API_KEY to your app secrets in Streamlit Cloud settings")
    st.info("Get your API key from: https://openrouter.ai/keys")
    st.stop()

# Initialize OpenRouter client for DeepSeek
if 'model' not in st.session_state:
    try:
        st.session_state['model'] = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
    except Exception as e:
        st.error(f"❌ Error initializing OpenAI client: {str(e)}")
        st.info("This might be a version compatibility issue. Please check the error logs.")
        st.stop()

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'chat_sessions' not in st.session_state:
    st.session_state['chat_sessions'] = {}

if 'current_session_id' not in st.session_state:
    st.session_state['current_session_id'] = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Create sidebar
st.sidebar.title("Settings")

# Chat History Management
with st.sidebar.expander("💬 Chat History", expanded=False):
    # New chat button
    if st.button("🆕 New Chat"):
        # Save current session if it has messages
        if st.session_state['messages']:
            st.session_state['chat_sessions'][st.session_state['current_session_id']] = {
                'messages': st.session_state['messages'].copy(),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'title': f"Chat {len(st.session_state['chat_sessions']) + 1}"
            }
        
        # Start new session
        st.session_state['current_session_id'] = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        st.session_state['messages'] = []
        st.rerun()
    
    # Display saved sessions
    if st.session_state['chat_sessions']:
        st.write("**Previous Chats:**")
        for session_id, session_data in reversed(list(st.session_state['chat_sessions'].items())):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if st.button(f"📝 {session_data['title']}", key=f"load_{session_id}"):
                    # Save current session before switching
                    if st.session_state['messages']:
                        st.session_state['chat_sessions'][st.session_state['current_session_id']] = {
                            'messages': st.session_state['messages'].copy(),
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'title': f"Chat {len(st.session_state['chat_sessions']) + 1}"
                        }
                    
                    # Load selected session
                    st.session_state['messages'] = session_data['messages'].copy()
                    st.session_state['current_session_id'] = session_id
                    st.rerun()
            
            with col2:
                if st.button("🗑️", key=f"delete_{session_id}", help="Delete this chat"):
                    del st.session_state['chat_sessions'][session_id]
                    st.rerun()
    
    # Clear all history
    if st.session_state['chat_sessions'] and st.button("🗑️ Clear All History"):
        st.session_state['chat_sessions'] = {}
        st.rerun()
    
    # Export chat history
    if st.session_state['messages']:
        chat_data = {
            'current_chat': st.session_state['messages'],
            'all_sessions': st.session_state['chat_sessions'],
            'exported_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        st.download_button(
            label="💾 Export Chat History",
            data=json.dumps(chat_data, indent=2),
            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

# Use DeepSeek V2.5 model
selected_model = "deepseek/deepseek-chat"

# Model parameters
temperature = st.sidebar.slider("🌡️ Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
max_tokens = st.sidebar.slider("📝 Max Tokens", min_value=1, max_value=4096, value=512)

# Add model description
with st.sidebar.expander("ℹ️ Model Info"):
    st.write("🚀 **DeepSeek V2.5**: Advanced model, excellent for complex reasoning and detailed responses.")

# Display current session info
if st.session_state['messages']:
    st.caption(f"💬 Current chat: {len(st.session_state['messages'])//2} messages")


for message in st.session_state['messages']:
   with st.chat_message(message['role']):
         st.markdown(message['content'])

#create chat interface

if prompt := st.chat_input("You: "):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # display a placeholder for the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

    # get the response from the DeepSeek model
    try:
        response = st.session_state['model'].chat.completions.create(
            model=selected_model,
            messages=st.session_state['messages'],
            temperature=temperature,
            max_tokens=max_tokens
        )

        # update the placeholder with the assistant's response
        assistant_response = response.choices[0].message.content
        message_placeholder.markdown(assistant_response)

        # append the assistant's response to the session state
        st.session_state['messages'].append({"role": "assistant", "content": assistant_response})
        
    except Exception as e:
        error_message = str(e)
        
        if "rate_limit" in error_message.lower() or "quota" in error_message.lower():
            error_response = """ **Rate Limit Reached**
            
You've hit the rate limit for this model. Try:

1. **Switch to Free Model**: Select "DeepSeek V2 Lite" (free tier)
2. **Wait a moment**: Rate limits reset quickly
3. **Check Credits**: Visit https://openrouter.ai/credits

DeepSeek models are usually very affordable or free!"""
        
        elif "unauthorized" in error_message.lower() or "api_key" in error_message.lower():
            error_response = """ **API Key Error**
            
Please check your OpenRouter API key:
1. Visit https://openrouter.ai/keys
2. Copy your API key
3. Update your .env file with: `OPENAI_API_KEY=your-key-here`"""
        
        else:
            error_response = f" **Error**: {error_message}\n\n💡 Try switching to the free DeepSeek model or check your API key."
        
        message_placeholder.markdown(error_response)
        st.session_state['messages'].append({"role": "assistant", "content": error_response})

# Footer with session info
if len(st.session_state['chat_sessions']) > 0:
    st.sidebar.markdown("---")
    st.sidebar.caption(f"📚 Total saved chats: {len(st.session_state['chat_sessions'])}")