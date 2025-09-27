# 🚀 Streamlit Cloud Deployment Guide

Follow these steps to deploy your DeepSeek AI Chatbot on Streamlit Cloud:

## 📋 Prerequisites

1. **GitHub Repository** - Your code should be pushed to GitHub
2. **OpenRouter API Key** - Get one from [OpenRouter](https://openrouter.ai/keys)
3. **Streamlit Account** - Sign up at [share.streamlit.io](https://share.streamlit.io)

## 🛠️ Deployment Steps

### Step 1: Prepare Your Repository

✅ Your repository should contain:
- `Chatbot.py` - Main application file
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `README.md` - Project documentation

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app"
   - Select your repository: `DevAyesh/Chatbot-with-Streamlit`
   - Set main file path: `Chatbot.py`
   - Choose a custom URL (optional)

3. **Configure Secrets**
   - Before deploying, click on "Advanced settings"
   - Go to "Secrets" tab
   - Add your API key:
   ```toml
   API_KEY = "your-openrouter-api-key-here"
   ```

4. **Deploy**
   - Click "Deploy!"
   - Wait for deployment to complete (2-3 minutes)

### Step 3: Test Your Deployment

1. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   
2. **Test Functionality**
   - Try sending a message
   - Adjust parameters in the sidebar
   - Verify error handling works

## ⚙️ Environment Configuration

### Local Development
```env
# .env file
API_KEY=your-openrouter-api-key
```

### Streamlit Cloud
```toml
# In Streamlit Cloud Secrets
API_KEY = "your-openrouter-api-key"
```

## 🔧 Troubleshooting

### Common Deployment Issues

**"API key not found" error:**
- Check that you've added `API_KEY` to Streamlit Cloud secrets
- Make sure the key is valid and has credits

**App won't start:**
- Check the logs in Streamlit Cloud dashboard
- Verify all dependencies are in `requirements.txt`
- Ensure file paths are correct

**Import errors:**
- Make sure all required packages are listed in `requirements.txt`
- Check package versions are compatible

### Getting Help

1. **Streamlit Cloud Logs**: Check the logs in your Streamlit dashboard
2. **OpenRouter Status**: Visit [OpenRouter](https://openrouter.ai) to check API status
3. **Community**: Ask questions on [Streamlit Community Forum](https://discuss.streamlit.io)

## 📱 App URL Structure

Your deployed app will be accessible at:
```
https://chatbot-with-streamlit-[random-id].streamlit.app
```

You can customize the URL during deployment or in your Streamlit Cloud dashboard.

## 🔄 Updates and Maintenance

### Updating Your App
1. Push changes to your GitHub repository
2. Streamlit Cloud will automatically redeploy
3. Check the deployment status in your dashboard

### Managing Secrets
1. Go to your Streamlit Cloud dashboard
2. Click on your app
3. Go to Settings → Secrets
4. Update API keys as needed

## 📊 Monitoring

### Usage Tracking
- Monitor your OpenRouter usage at [OpenRouter Dashboard](https://openrouter.ai/activity)
- Set up usage alerts if needed

### App Analytics
- View app usage in Streamlit Cloud dashboard
- Monitor performance and errors

---

**🎉 Your DeepSeek AI Chatbot is now live on the web!**

Share your app URL with others and enjoy chatting with DeepSeek AI!