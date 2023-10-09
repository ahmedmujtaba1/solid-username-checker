import requests, random

def check_existence(email:str) -> bool:
    url = f"https://api.apilayer.com/email_verification/check?email={email}"

    payload = {}
    api_keys = ['JvsouKusHXQGhLZ2A6Ukh93jFYAdrjqs',"C4XTOR0gK7531jTKBdpGJtGYkJh5x54B","5tAckRNOPmkRUkudQm07DRG8PKcYB3tm"]
    headers= {
        "apikey": random.choice(api_keys)
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()
    # print("Results : ", result)
    return result['mx_found']

# print(check_existence('ahmedkdjkddodikolk@mail.com'))