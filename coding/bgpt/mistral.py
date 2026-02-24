import requests

API_KEY = ""
url = "https://apim-azr-ue2-bgpt-prd-ucin.azure-api.net/"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

user_prompt = input("Enter your prompt: ")

data = {
    "model": "mistral-document-ai-2505",  # or "mistral-small", "mistral-medium"
    "messages": [
        {"role": "system", "content": "You are a chatbot assistant. You are helping a user with a task."},
        {"role": "user", "content": user_prompt}
    ],
    "temperature": 1,
    "top_p": 1,
    "max_tokens": 5000
}

response = requests.post(url, headers=headers, json=data)
print("Response:")
print(response.json())
