# 🚀 OpenRouter AI Chatbot

Welcome to the **OpenRouter AI Chatbot**! This guide will help you set up and run the chatbot with **Streamlit**. Follow the steps below to get started. 🤖✨

---

## 📌 Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- `pip` (Python package manager)
- Virtual environment (`venv`)

---

## 🛠️ Setup Guide

### 1️⃣ Get an API Key 🔑
Sign up at [OpenRouter.ai](https://openrouter.ai/) and obtain your API key.

### 2️⃣ Activate Virtual Environment 🌍
```bash
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python -m venv env
source env/bin/activate
```

### 3️⃣ Install Dependencies 📦
```bash
pip install -r requirements.txt
```

### 4️⃣ Set the API Key in Code 🔧
Modify your **chatbot.py** file to include your API key:
```python
API_KEY = "api.key"  # Replace with your OpenRouter key
```

### 5️⃣ Run the Chatbot 🚀
```bash
streamlit run chatbot.py
```

---

## 🎭 Usage
Once the chatbot is running, you can interact with it via the Streamlit interface in your browser. Enjoy chatting with AI in real-time! 🗨️🤖

---

## 💡 Troubleshooting
- If `venv` doesn’t activate, try running the command as administrator.
- Ensure `requirements.txt` is correctly installed.
- If issues persist, refer to the OpenRouter AI documentation.

---

## 🎉 Happy Coding!
Now you’re all set to explore and enhance your chatbot! 🚀✨

