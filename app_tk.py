import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import os

# API setup
API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyBRZFATvn0Wi47zQY_4BZzAnfm8Wv5yYe0"
genai.configure(api_key=API_KEY)

# Model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def send_message():
    user_msg = entry.get()
    if not user_msg.strip():
        return
    chat_window.insert(tk.END, f"You: {user_msg}\n", "user")
    entry.delete(0, tk.END)

    response = chat.send_message(user_msg)
    bot_msg = response.text
    chat_window.insert(tk.END, f"Gemini: {bot_msg}\n\n", "bot")

# Tkinter UI
root = tk.Tk()
root.title("Gemini AI Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(padx=10, pady=5, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(padx=5, pady=5, side=tk.LEFT)

root.mainloop()
