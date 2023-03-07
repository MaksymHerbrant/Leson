import requests 

url = 'https://api.openai.com/v1/completions'

headers = {"Content-Type" : "application/json", "Authorization": "Bearer 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",
           "OpenAI-Organization" : "org-R69C3BkuUCUBCT5g4tIMDaqa" }

data = {"model": "text-davinci-003",
        "prompt": "КАк дела?",
        "max_tokens": 200,
        "temperature": 0}

print(requests.post(url, headers=headers, json=data).text)