#!/usr/bin/python3
"""Send requests with a header"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    headers = {
            "email": argv[2]
            }
    resp = requests.post(url, data=headers)
    print(resp.text)
