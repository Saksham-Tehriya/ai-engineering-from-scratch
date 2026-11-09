import os
from dotenv import load_dotenv
from groq import Groq

# Load the hidden .env file
load_dotenv() 

# Pull the Groq key from memory
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("Error: Could not find GROQ_API_KEY in the .env file.")
else:
    # Connect to the free AI
    client = Groq(api_key=api_key)

    # Send the prompt
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
        model="openai/gpt-oss-120b", 
    )

    # Print the answer
    print(f"AI Response: {response.choices[0].message.content}")