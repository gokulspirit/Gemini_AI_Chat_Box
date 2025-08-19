import streamlit as st
import google.generativeai as genai
import os

# Configure API
API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyBRZFATvn0Wi47zQY_4BZzAnfm8Wv5yYe0"
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Page setup
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Gemini AI Chatbot")
st.caption("Built with Streamlit + Google Generative AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
if prompt := st.chat_input("Say something..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Gemini response
    response = chat.send_message(prompt)
    reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
#run this comment streamlit run app_ui.py