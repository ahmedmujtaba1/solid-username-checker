# # from email_validate import validate_or_fail

# # valid  = validate_or_fail(
# #             email_address="ahmed@gmail.com",
# #             check_smtp=True,
# #             check_dns=True,
# #             # smtp_debug=True
# #         )
# # print(valid)

# from validate_email_address import validate_email

# print(validate_email(email="HikingAdventures@gmail.com", verify=True))

from verify_email import verify_email
from email_validate import validate_or_fail

# print(validate_or_fail("rustomdeveloper@gmail.com",check_dns=False, check_smtp=False, check_format=False, check_blacklist=True))



# email = "johnsmith@gmail.com".lower()
# # print(validate(email))
# import requests, json

# formdata1 = {
#     "emails" : "khizranmohsi22n%40gmail.com",
# }

# formdata = json.dumps(formdata1)

# r = requests.post("https://www.site24x7.com/tools/email-validator", data=formdata)
# print(r.content)
import requests
import json
import re
from bs4 import BeautifulSoup

def userExists(username, s):
    print("Checking the availability of {}".format(username))
    link = 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = s.get(link, headers=headers).text
    except:
        print("Failed to open {}".format(link))
        return None
    specData = re.findall(r'value="(.*?)" name="specData"', resp)[0]
    crumb = re.findall(r'value="(.*?)" name="crumb"', resp)[0]
    acrumb = re.findall(r'value="(.*?)" name="acrumb"', resp)[0]
    sessionIndex = re.findall(r'value="(.*?)" name="sessionIndex"', resp)[0]
    link = "https://login.yahoo.com/account/module/create?validateField=yid"
    headers = {
        'Referer': 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-360,"timezone":"Asia/Dhaka","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"1","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0, D3D11-20.19.15.4380)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1624081774716,"render":1624081773747}}',
        'specId': 'yidregsimplified',
        'cacheStored': '',
        'crumb': crumb,
        'acrumb': acrumb,
        'sessionIndex': sessionIndex,
        'done': 'https://mail.yahoo.com/d?pspid=2023538075&activity=ybar-mail',
        'googleIdToken': '',
        'authCode': '',
        'attrSetIndex': '0',
        'specData': specData,
        'multiDomain': '',
        'tos0': 'oath_freereg|us|en-US',
        'firstName': '',
        'lastName': '',
        'userid-domain': 'yahoo',
        'userId': username,
        'password': '',
        'phone': '',
        'mm': '',
        'dd': '',
        'yyyy': '',
        'signup': '',
    }
    try:
        resp = s.post(link, headers=headers, data=data).json()
    except:
        print("Failed to open {}".format(link))
        return None
    # print(resp)
    all_errors = resp.get('errors', [])
    if len(all_errors) == 0:
        return None
    for errors in all_errors:
        if errors.get('name') == "userId":
            # print(errors.get('error'))
            return True
    return False

s = requests.Session()
print(userExists(username="aksjkjskslsks", s=s))