#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""

from sys import argv
import requests

if __name__ == "__main__":
    try:
        value = {"q": argv[1]}
    except IndexError:
        value = {"q": ""}
    finally:
        resp = requests.post("http://0.0.0.0:5000/search_user", data=value)
        try:
            data = resp.json()
            if data:
                print("[{}] {}".format(data['id'], data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
