from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.title("DeepSeek AI Chatbot")

# Check if API key is set
api_key = os.getenv("API_KEY")

if not api_key:
    st.error(" OpenRouter API key not found!")
    st.stop()

# Initialize OpenRouter client for DeepSeek
if 'model' not in st.session_state:
    st.session_state['model'] = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Create sidebar to adjust parameters
st.sidebar.title("Settings")

# Use DeepSeek V2.5 model
selected_model = "deepseek/deepseek-chat"

# Model parameters
temperature = st.sidebar.slider("🌡️ Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
max_tokens = st.sidebar.slider("📝 Max Tokens", min_value=1, max_value=4096, value=512)

# Add model description
with st.sidebar.expander("Model Info"):
    st.write("🚀 **DeepSeek V2.5**: Advanced model, excellent for complex reasoning and detailed responses.")


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