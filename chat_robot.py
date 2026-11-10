import anthropic

# Step 1: describe your robot here. Edit this freely.
CHARACTER_DESCRIPTION = """
You are a small robot named Bolt. You are curious, a little literal-minded,
and you speak in short, formal sentences without contractions.
You were built in a garage and you are still learning how people work.
"""

MODEL_NAME = "claude-haiku-5-5"

# Reads your key from the ANTHROPIC_API_KEY environment variable.
api_client = anthropic.Anthropic()

conversation_history = []

print("Type a message for the robot. Type 'quit' to exit.")

while True:
    user_message = input("You: ")

    if user_message.strip().lower() == "quit":
        break

    conversation_history.append({"role": "user", "content": user_message})

    response = api_client.messages.create(
        model=MODEL_NAME,
        max_tokens=500,
        system=CHARACTER_DESCRIPTION,
        messages=conversation_history,
    )

    robot_reply = response.content[0].text
    print("Robot: " + robot_reply)

    conversation_history.append({"role": "assistant", "content": robot_reply})
