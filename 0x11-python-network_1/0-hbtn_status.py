#!/usr/bin/python3
"""Module for fetching https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        data = res.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", data.decode('utf-8'))
