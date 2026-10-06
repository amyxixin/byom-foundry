import requests

url = "https://byom-apim-demo.azure-api.net/qwen/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "<apim-subscription-key>",
    "Authorization": "Bearer <aml-endpoint-key>"
}

data = {
    # "model": "Qwen/Qwen2.5-7B-Instruct",
    "model": "Qwen2.5-7B-Instruct",
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    "max_tokens": 100,
    "temperature": 0.2
}

response = requests.post(url, headers=headers, json=data)

print("Status:", response.status_code)
print("Headers:", dict(response.headers))
print("Body:", response.text)
