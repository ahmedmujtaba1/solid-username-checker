import requests, secrets, string
from bs4 import BeautifulSoup

print("[+] Hello Everyone! This is the bot for checking that your username on yahoo exists or not. For stopping type 'q' or 'quit' to quit this bot.")
print('[+] Made By Ahmed Mujtaba Mohsin.')

while True:
    user_username = input('[+] Enter your username to check: ')
    if user_username == "q" and user_username == "q":
        break
    xsrf_token = f"eyJpdiI6IjNEMnBTS1NrWm9OVXNzRldSOWFQTnc9PSIsInZhbHVlIjoiSWRQUnRCM3M5eUlzc1MwM2VBWkdSV3oxZnlLWGpJNE5xMjVHY0N1c3lhSncvMXZNalFJbnJOU2Q1ZXhPRkVFM0pkOUpMNWpJbU91RGZUODlmMy96UU1jK3pYRTFZbVRmSStrODlRQ0l2MVVOUFJWenRvUWJvNHRKQk5CSXp6TTciLCJtYWMiOiI1NGRhZDNhZGIxNjhlMTUyNGFmMWRhZmNiNWFhODhjOGMyZjdkYWE4MjAyN2ZiZDhkYjhmZTM1YzljNWEzMTAzIiwidGFnIjoiIn0%4D"
    # token_length = 64 
    # characters = string.ascii_uppercase + string.digits + '+/='
    # xsrf_token = ''.join(secrets.choice(characters) for _ in range(token_length))
    headers = {
        'authority' : "mailbite.io",
        "method" : "POST",
        "path" : "/check-email-verify",
        "scheme" : "https",
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip, deflate, br",
        'Accept-Language' : 'en-US,en;q=0.9',
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length" : "81",
        "Origin" : "https://mailbite.io",
        "Referer" : "https://mailbite.io/?gclid=Cj0KCQjwmvSoBhDOARIsAK6aV7hzJTYAxOBiWyaWH9K8wGPhRgIHh4CgTlqLWLluii22lIIJEpqx1j0aAvXSEALw_wcB",
        "X-Requested-With" : "XMLHttpRequest",
        "Sec-Fetch-Mode" : "cors",
        "Sec-Fetch-Site" : "same-origin",
        "Sec-Fetch-Dest" : "empty",
        "Cookie" : f"_ga_RTWSCL7TYX=GS1.1.1696470044.1.0.1696470044.0.0.0; _ga=GA1.1.1350925821.1696470044; _gcl_aw=GCL.1696470045.Cj0KCQjwmvSoBhDOARIsAK6aV7hzJTYAxOBiWyaWH9K8wGPhRgIHh4CgTlqLWLluii22lIIJEpqx1j0aAvXSEALw_wcB; _gcl_au=1.1.269977082.1696470045; XSRF-TOKEN={xsrf_token}; saasproject_session=eyJpdiI6ImNJRDdtZ0c3V3ZGWXpnNXgvbUI5NFE9PSIsInZhbHVlIjoiQVNMdVR1UmE2WUJiR0VRWnEwTWx5ZHBiZWlmU25VZC91TUcvN0FGVlZYS3o4VVhjby9IMjdOZGkyMUtBY2dWWDdNdFA2dE1Wb2tpMXRjN1NrRWFCaUZlanY0MDdhcTJlQzV1UTJjQzY1ZkpzMm1ubGw3UjBvS0Q2S1VIRmRxQXQiLCJtYWMiOiIxNWFiZTViZjIyMWM1ZDgxNTJjM2JiYjI4MzY0YWVjYzViZjVhNWI0MjQyYTlkZTM4MzVjNzM2ODI0MmZiMDJmIiwidGFnIjoiIn0%3D; d2olEYjakiot1zcbmzC7ycsnEMoA0uDxljwBZePS=eyJpdiI6InFCemdvNU5TYlhOZXRwSEk5eGFZeWc9PSIsInZhbHVlIjoiM0ptQ0t1bHljcU9rem1pN3pSdkxTMjkzdWQ1cmttZXR3aDcyMzhSSzl0ZDhJMlFDKzZzOHpYQndaZEJzaFZUTHVrMlFXcjVrT05OU002ZGpuVHBNcUlDaDVXYThhU3RiSFp0TXBYTTBaN0hnUE5UYUxFcnFnZ0MvbUwyNVZxR2dEOTV3bU9pK3NIK09OSzdTai9PRWNnMkdDa0FBa2ZjOXJ5MjYxSExuZ0xpaWsvVEVHSGh3cDhGK2Q4UWZodFhUMlNmanJtU0NLTStHTFAyQ0pTVnRJQmYvYzdtM3VQUGQrVFNJRG1LRVVKYmplUTBOblRKY3RMdlRnR2xLZ1hneFE4dXE2dmNwVW9PTkRmQ3puNU4rbWhzK1IrcmZxdlZlZjBtY0QzVUFxZy9QSVBJUG4vOWpWUlBUZlFHYzM5RnFCUktiMEl0WGl2WHZHRDBqMndMK21sa1BYZGh6VWZFUmZmODRIL0JMTDkrQzByWE9FZXZObWtteENyMnowV0NvSjlQbU1iQnJ6YXpZUGJuZ3NLWjJhWUVWM2F5SjdsVVB5VlhTQ0l5RDA4NUR2TWozS2JrVDhKVEg4QUcxOHJXY05zcXlhSG1adFN5SHlaOGErZHZEbnlucDZEQm1JVG95SmFrQmZ5R0hHNStHV3dOeU1zRk1tZWpBV0E2aUowYUUiLCJtYWMiOiI5OTI4NTVlOGFmYWRlZDMxM2RiZTJmNzIzNmJjN2U3MTU2ZjQ2Y2MxYjk1OThlZDAxMTJkOWM5ZWNkYTRmZTBjIiwidGFnIjoiIn0%3D; arp_scroll_position=293.3333435058594",
        # 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", 
    }

    formdata = {
        '_token' : 'jNkFzEdG46vQiko5g2RmCrrXXoKUdqGixSIs5BEI',
        'email' : f'{user_username}@yahoo.com'
    }

    r = requests.api.post('https://mailbite.io/check-email-verify',headers=headers, data=formdata)
    print(r.text)
    # if "A Yahoo account already exists with this email address" in str(variable):
    #     print("Your username is exist on yahoo.com")
    # else:
    #     print("Your username is not exist on yahoo.com")
    print('--------------------------------------------------')
