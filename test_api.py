import requests

url = "https://dry-buckets-cheer.loca.lt/api-endpoint"
data = {
    "email": "student@example.com",
    "secret": "mytdssecret2025",
    "task": "captcha-solver-001",
    "round": 2,
    "nonce": "12345",
    "brief": "Create a captcha solver",
    "checks": ["Page loads", "Captcha solved"],
    "evaluation_url": "https://example.com/notify",
    "attachments": []
}

response = requests.post(url, json=data)
print(response.status_code, response.text)
