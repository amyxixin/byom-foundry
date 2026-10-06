import requests
import json

url = "https://qwen7b-endpoint.canadacentral.inference.ml.azure.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <aml-endpoint-api-key>"
}

data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
