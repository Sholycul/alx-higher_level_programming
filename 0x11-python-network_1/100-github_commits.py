#!/usr/bin/python3

""" Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
- Displays the body of the response.
"""

import requests
import sys


def fetch_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <repository_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repo_name, owner_name)
