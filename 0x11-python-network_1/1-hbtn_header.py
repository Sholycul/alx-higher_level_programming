#!/usr/bin/python3
"""File that takes a URL, sends a request and display the value of the
X-Request-Id
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.info()
        x = data.get("X-Request-Id")
        print(x)
