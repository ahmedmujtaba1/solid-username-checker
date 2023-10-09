
import requests


def check_email(email):
    api_keys = ["eb575a764e044b8d9716922b470e500e",]
    response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=&email={email}")
    print(response.status_code)
    r = response.json()
    return r["is_smtp_valid"]["value"]

check_email('ahmed@gmx.com')