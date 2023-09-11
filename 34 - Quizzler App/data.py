import requests

parameters = {"amount": 10, "category": 15, "type": "boolean"}
api_url = "https://opentdb.com/api.php"

question_data = requests.get(url=api_url, params=parameters)
question_data.raise_for_status()
question_data = question_data.json()["results"]
