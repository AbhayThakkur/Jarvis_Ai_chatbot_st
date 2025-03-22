import streamlit as st
import time
import random
import requests

API_KEY = "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"  # Replace with your OpenRouter key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def chat_with_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-small-3.1-24b-instruct:free",  # Or use GPT-4, Claude, etc.
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Run chatbot
# while True:

# Page title and UI setup
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("🤖 Jarvis")

# Custom CSS for chat styling
st.markdown(
    """
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .user-message, .bot-message {
            padding: 12px;
            border-radius: 18px;
            margin: 8px 0;
            display: inline-block;
            max-width: 80%;
        }
        .user-message {
            background-color: #c5d5dc;
            color: white;
            text-align: right;
            float: right;
            clear: both;
        }
        .bot-message {
            background-color: #E5E5EA;
            color: black;
            text-align: left;
            float: left;
            clear: both;
        }
        .chat-input-container {
            position: fixed;
            bottom: 10px;
            width: 100%;
            background-color: white;
            padding: 10px;
            box-shadow: 0px -2px 10px rgba(0,0,0,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat history
for message in st.session_state.messages:
    align_class = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(f"<div class='chat-container'><div class='{align_class}'>{message['content']}</div></div>", unsafe_allow_html=True)

# User input
st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
user_input = st.chat_input("Ask me anything...")
st.markdown("</div>", unsafe_allow_html=True)

if user_input:
    # Store and display user message on the right
    user_message = f"❤️‍🔥: {user_input}"
    st.session_state.messages.append({"role": "user", "content": user_message})
    st.markdown(f"<div class='chat-container'><div class='user-message'>{user_message}</div></div>", unsafe_allow_html=True)

    # Simulate bot typing delay
    time.sleep(random.uniform(0.5, 1.5))
    
    # Generate bot response (Replace with your chatbot logic)
    bot_response = f"💗: {chat_with_openrouter(user_input)}"  # Dummy response
    
    # Store and display bot response on the left
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.markdown(f"<div class='chat-container'><div class='bot-message'>{bot_response}</div></div>", unsafe_allow_html=True)
    

