import requests

payload = {
    "email": "student@example.com",
    "task": "captcha-solver-001",
    "round": 2,
    "nonce": "12345",
    "repo_url": "https://github.com/ashal994/iitm-tds-project",
    "commit_sha": "f3e997dd9aa50a0a059c2be1551dcbbd79bbb616",  # use your latest SHA
    "pages_url": "https://ashal994.github.io/iitm-tds-project/"
}

evaluation_url = "https://example.com/notify"  # placeholder

response = requests.post(evaluation_url, json=payload)
print(response.status_code, response.text)
