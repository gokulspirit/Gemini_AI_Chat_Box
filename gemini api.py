import google.generativeai as genai

API_KEY = "AIzaSyBRZFATvn0Wi47zQY_4BZzAnfm8Wv5yYe0"
genai.configure(api_key=API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    
    # Print response
    print("Gemini:", response.text)
# use case go to aistudio.google.com create api .then pip install google-generativeai . now your code is work
