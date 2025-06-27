import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

def get_pr_diff(pr_url):
    response = requests.get(pr_url, headers=HEADERS)
    return response.text

def post_comment(repo, pr_number, comment):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    payload = {"body": comment}
    requests.post(url, json=payload, headers=HEADERS)