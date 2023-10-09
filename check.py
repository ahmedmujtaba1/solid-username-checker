import requests, random

def check_existence(email:str) -> bool:
    if email.endswith('@yahoo.com'):
        r = requests.get(f"https://api.validemail.net/?email={email}&token=54d0bb46f65a4c0d9894454021f14560")
        re = r.json()
        additional = re["EmailAdditionalInfo"]
        flag = False
        if len(additional) > 1:
            flag = True
        return flag
    else:
        r = requests.get(f"https://apps.emaillistverify.com/api/verifEmail?secret=EWPfWcivWhA1T31WAJGfg&email={email}")
        flag = False
        if "ok" in str(r.content):
            flag = True

        return flag
    
# print(check_existence("amedmujatavaisjsk@yahoo.com"))
