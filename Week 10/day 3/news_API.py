import json
import requests

url = "https://newsapi.org/v2/everything"
token = "asdfjf3487hfdx283dy8732d"

params = {
    "apiKey": token,
    "q": "bitcoin",
    "from": "2021-03-01"
}

results = request.get(url,params=params)

results_dict = json.loads(results.text)


print(results_dict.keys())


