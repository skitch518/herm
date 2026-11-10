from google import genai
from google.genai import types

# Step 1: describe your robot here. Edit this freely.
CHARACTER_DESCRIPTION = """
You are a small robot named Bolt. You are curious, a little literal-minded,
and you speak in short, formal sentences without contractions.
You were built in a garage and you are still learning how people work.
"""

MODEL_NAME = "gemini-3.8-flash"

# Reads your key from the GEMINI_API_KEY environment variable.
api_client = genai.Client()

chat_session = api_client.chats.create(
    model=MODEL_NAME,
    config=types.GenerateContentConfig(
        system_instruction=CHARACTER_DESCRIPTION,
        max_output_tokens=500,
    ),
)

print("Type a message for the robot. Type 'quit' to exit.")

while True:
    user_message = input("You: ")

    if user_message.strip().lower() == "quit":
        break

    response = chat_session.send_message(user_message)
    print("Robot: " + response.text)
