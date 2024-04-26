#!/usr/bin/python3
"""Returns email"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {
            "email": argv[2]
        }

    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")
    re = urllib.request.Request(url, data)
    with urllib.request.urlopen(re) as response:
        page = response.read()
        print(page.decode("utf-8"))
