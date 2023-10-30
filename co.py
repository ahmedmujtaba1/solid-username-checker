import requests
import json
import re
from bs4 import BeautifulSoup
from verify_email import verify_email

# def verify(email, ouputAlive = None):
# 	url = "https://mail.google.com/mail/gxlu?email={}".format(email)
# 	print(url)
# 	headers = {
# 		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# 	}
# 	resp_headers = requests.get(url=url, headers=headers).headers
# 	if "Set-Cookie" in resp_headers:
# 		if ouputAlive == 1:
# 			return "Alive"
# 		else:
# 			pass
# 	else:
# 		return "Unregistered"


# # check = verify_email('HeatherLewis234@gmail.com')
# check = verify('hikingadventures@gmail.com', 1)
# print('GMAIL CHECKER : ', check)

# Url_Get_Cookies = "https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.com%2F&hl=en&dsh=S-553617478%3A1614242741811960&gmb=exp&biz=false"
# cookies = ""

# def get_cookie():
#     global cookies
#     ress = requests.get(Url_Get_Cookies, headers={"Cookie": "1P_JAR=2021-02-23-19; NID=210=IaV6oTvVVkYHNAF4jAd6QCgzeVwo8H6_-WrWJX8468zCf4p6izAYX0CIggELGI-ETd_s3StcGbVyL18sOiLgGlEHQQ8IeeMSFWiQazsJD69QOeAQVDGIlSQe3KbY70rfkYH9tSSbmIKJPwsKNy7fr2YH8H-UqIpAIiNl5Nawf7w","X-Requested-With":"com.android.browser","ContentType":"application/x-www-form-urlencoded;charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; G011A Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36"})
#     cookies ="AEThL"+ re.search("&quot;AEThL(.*?)&quot", ress.text).groups(0)[0]

# def check(email):
#         try:
#             headers = {
#                 'User-Agent': "Mozilla/5.0 (Linux; Android 7.1.2; G011A Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36",
#                 'Cookie': f"1P_JAR=2021-02-23-19; NID=210={cookies}; __Host-GAPS=1:GV8kzgewC2diEGhLxP46yc0RnUbE3w:b2UyjKc8vOsTSKWu",
#                 'ContentType': "application/x-www-form-urlencoded;charset=UTF-8",
#                 'Host': "accounts.google.com",
#                 'Accept': "application/json",
#                 'Content-Type' : "application/json",
#                 "Google-Accounts-XSRF": "1"
#             }
#             data = {'continue': 'https://www.google.com/?gws_rd=ssl&dsh=S486615459:1614110174398934', "hl": "ar",
#                     "flowName": "GlifWebSignIn", "flowEntry": "SignUp",
#                     "f.req": "[" + cookies + ",""by404.erroz"",""its""," + email + ",false]",
#                     "azt": "AFoagUV7a5sfFTSy_fbzkMiYW9ZXRGkAcA:1614155570432", "cookiesDisabled": "false",
#                     "deviceinfo": "[null,null,null,[],null,SA,null,null,[],GlifWebSignIn,null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,0,null,false]",
#                     "gmscoreversion": "undefined"}
#             response = requests.post(
#                 "https://accounts.google.com/_/signup/usernameavailability?hl=en&TL=AIBe4_IksfGwbXbrPiWl_SDtdo6sWPUh2U61Gl_2HtUXwN-zzwfU3r7tJeV8l_2D&_reqid=423175&rt=j", data=data,
#                 headers=headers)
#             print("Response : ", response.json())
#             if '[[["gf.wuar",1,[]' in response:
#                return True
#             elif '[[["er",null,null,null,null,400,null,null,null,3]' in response:
#                 get_cookie()
#                 check(email)
#             else:
#                 return False
#         except Exception:
#              get_cookie()
#              check(email)


# print(check("rustomdeveloper@gmai"))


def userExists(username, s):
    print("Checking the availability of {}".format(username))
    link = 'https://login.aol.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail'
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
    link = "https://login.aol.com/account/module/create?validateField=userId"
    headers = {
        'Referer': 'https://login.aol.com/account/create?lang=de-de&src=mail&activity=default&pspid=1197803637&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Dde-de%26nonce%3DAsnCalu9BnQWnSvRvYA0WjA9kGD7DBtz%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL3dlYm1haWwtc3RkL2RlLWRlL3N1aXRlIn0.ee3Ui8nuj5ekOowTgO2alBKl4GyZtt0SpxK6i2jNoAJdFNK0A55U-bzNkD9rYv_yFDbmDoshkper86SPUHIdB0X2i0pi697RiMLnotLZfFgAOoN4Pq5j98SpoxIJwFMokswltYaNM4q-ZSFk8fiOAlOm1TNMpX_B3KAzLhgbq8w&specId=yidregsimplified',
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
        'done': 'https://mail.aol.com/d?pspid=2023538075&activity=ybar-mail',
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
check = userExists(username="ahmed@aol.com", s=s)