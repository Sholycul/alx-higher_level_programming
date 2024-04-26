#!/usr/bin/python3
"""My profile id"""
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/users/{argv[1]}"

    headers = {"accept": "application/vnd.github+json",
               "Authorization": f"Bearer {argv[2]}"}

    response = requests.get(url, headers=headers)
    profile = response.json()

    idx = profile["id"]
    print(idx)
