from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Replace with your actual API key
API_KEY = os.getenv("GPT_4_1_API_KEY")

# Endpoint URL

url = "https://apim-azr-ue2-bgpt-prd-ucin.azure-api.net/openai/deployments/gpt-4.1-ptu/chat/completions?api-version=2025-04-01-preview"

# User prompt
user_prompt = input("Enter your prompt: ")

# Request headers
headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

# Request body
data = {
    "temperature": 1,
    "top_p": 1,
    "stream": False,
    "max_completion_tokens": 5000,
    "messages": [
        {
            "role": "system",
            "content": "You are a chatbot assistant. You are helping a user with a task."
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
}

# Send POST request
response = requests.post(url, headers=headers, json=data)

# Print response
print("Response:")

response_json = response.json()
assistant_message = response_json['choices'][0]['message']['content']
print(assistant_message)
