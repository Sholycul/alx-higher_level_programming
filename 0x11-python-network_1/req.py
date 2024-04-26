#!/usr/bin/python3
import requests


token = "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"

url = "https://api.github.com/users/Sholycul"

headers = {"accept": "application/vnd.github+json","Authorization": "Bearer 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"}


response = requests.get(url, headers=headers)
print(response.json()["id"])
