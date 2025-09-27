# 🤖 DeepSeek AI Chatbot

A modern, interactive chatbot built with Streamlit and powered by DeepSeek AI through OpenRouter. This chatbot provides an intuitive chat interface with customizable parameters for engaging conversations.

## ✨ Features

- 🎯 **DeepSeek V2.5 Integration** - Powered by advanced DeepSeek AI model
- 💬 **Interactive Chat Interface** - Clean, modern chat UI with message history
- ⚙️ **Customizable Parameters** - Adjust temperature and max tokens
- 🔒 **Secure API Key Management** - Environment-based configuration
- ❌ **Error Handling** - Graceful handling of API errors and rate limits
- 🎨 **Streamlit UI** - Beautiful, responsive web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenRouter API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Chatbot with Streamlit"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   
   # Windows Command Prompt
   .venv\Scripts\activate.bat
   
   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   API_KEY=your-openrouter-api-key-here
   ```

6. **Run the application**
   ```bash
   # Make sure virtual environment is activated first
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   streamlit run Chatbot.py
   ```

## 🔑 Getting Your API Key

1. Visit [OpenRouter](https://openrouter.ai/keys)
2. Sign up for a free account
3. Get free credits ($1-5) upon registration
4. Copy your API key
5. Add it to your `.env` file

## 📁 Project Structure

```
Chatbot with Streamlit/
├── Chatbot.py          # Main application file
├── .env               # Environment variables (not in git)
├── .gitignore         # Git ignore rules
├── .venv/             # Virtual environment
└── README.md          # This file
```

## ⚙️ Configuration

### Model Settings

The chatbot uses **DeepSeek V2.5** (`deepseek/deepseek-chat`) model by default.

### Adjustable Parameters

- **Temperature** (0.0 - 2.0): Controls response creativity
  - Lower = More focused and deterministic
  - Higher = More creative and varied

- **Max Tokens** (1 - 4096): Maximum response length
  - Adjust based on desired response length

## 🛠️ Usage

1. **Start the application** using `streamlit run Chatbot.py`
2. **Open your browser** to the provided local URL (usually `http://localhost:8501`)
3. **Adjust settings** in the sidebar if needed
4. **Start chatting** by typing in the input box at the bottom
5. **View conversation history** as you chat

## 🔧 Troubleshooting

### Common Issues

**"OpenRouter API key not found!"**
- Make sure your `.env` file exists and contains `API_KEY=your-key-here`
- Restart the application after adding the API key

**Rate Limit Errors**
- Wait a moment and try again
- Check your OpenRouter credits at https://openrouter.ai/credits
- Consider upgrading your plan if needed

**Import Errors**
- Make sure you've activated your virtual environment
- Install missing packages: `pip install streamlit openai python-dotenv`

## 💡 Tips

- **Free Usage**: OpenRouter provides free credits for new users
- **Cost Effective**: DeepSeek models are very affordable
- **Conversation History**: Your chat history is maintained during the session
- **Customization**: Adjust temperature and tokens for different conversation styles

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- [OpenRouter](https://openrouter.ai/) - API Provider
- [DeepSeek AI](https://deepseek.com/) - AI Model
- [Streamlit](https://streamlit.io/) - Web Framework
- [OpenAI Python Library](https://github.com/openai/openai-python) - API Client

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Visit [OpenRouter Documentation](https://openrouter.ai/docs)
3. Create an issue in this repository

---

**Built with ❤️ using Streamlit and DeepSeek AI**
