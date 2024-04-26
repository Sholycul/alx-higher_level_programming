#!/usr/bin/python3
"""Response code"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as re:
            data = re.read()
            print(data.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
