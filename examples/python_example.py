"""
Tokener Pro — Python Example
OpenAI-compatible Minimax API
"""

from openai import OpenAI

# Initialize client with Tokener Pro endpoint
client = OpenAI(
    api_key="YOUR_TOKENER_API_KEY",  # Get from https://renrenfa.top/dashboard
    base_url="https://renrenfa.top/v1"
)

# Text completion
def chat():
    response = client.chat.completions.create(
        model="minimax-01",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
        temperature=0.7
    )
    print(response.choices[0].message.content)

# Image generation
def image():
    response = client.images.generate(
        model="minimax-t2i",
        prompt="A beautiful sunset over Paris",
        size="1024x1024"
    )
    print(response.data[0].url)

if __name__ == "__main__":
    print("=== Chat Example ===")
    chat()
    print("\n=== Image Example ===")
    image()
