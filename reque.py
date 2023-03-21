import requests

response = requests.get('http://127.0.0.1:8000/api/snippets')
print(response.json())

payload = {
    "title":"title"
}
response = requests.post('http://127.0.0.1:8000/api/snippets', data=payload)
print(response.content)
