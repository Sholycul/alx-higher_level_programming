#!/usr/bin/python3
"""Request header"""
import requests
from sys import argv

if __name__ == "__name__":
    url = argv[1]
    res = requests.get(url)
    x_id = res.headers.get("X-Request-Id")

    print(x_id)
