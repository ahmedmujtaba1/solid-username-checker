
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

def gmx_checker(email: str):
    headers = {
        # 'Accept-Encoding' : 'gzip, deflate, br',
        'Accept' : "application/json",
        # 'Cache-Control' : 'no-cache',
        # 'Connection' : 'keep-alive',
        # 'Content-Length' : '175',
        'Content-Type' : "application/json",
        # 'Authorization' : 'Bearer qXeyJhbGciOiJIUzI1NiJ9.eyJjdCI6IlRmMXlnNDhTSzV6X1NYUEo2ekZMdFVmU0JvblpVWVFLWmNWcDlXeGxabkpFZmFHWU5CUEhFS3gyTEszNDcxNzMtdDQxOV9HVEJOdVhYdk5JUW15OFY4bU1Ua1ZFLVZocU1GTEwxRjFtd2xmN3RDQTRkYTQxdDFmQmpPM3laNUtMczBTcGhGVDVjRjd0UVpXM2Z2ZGdQQzA5dG04NFRJenRQM0ZCZ1ZEMkdkayIsInNjb3BlIjoicmVnaXN0cmF0aW9uIiwia2lkIjoiN2U0ZjQ2NDkiLCJleHAiOjE2OTg2MDYwOTM5MTIsIml2IjoieUttZDhXTHY3aTFoSk5NcHVncVNHUSIsImlhdCI6MTY5ODYwMjQ5MzkxMiwidmVyc2lvbiI6Mn0.PjSO-zERQpcpuzeYifIOcTiQt1YjZjB3SJvf_pFeD7E',
        # 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}
    data = {
        "emailAddress"  : "ahmed@gmx.com",
	}
    data = json.dumps(data)
    r = requests.post('https://signup.gmx.com/suggest/rest/email-alias/availability', headers=headers, data=data)
    print(r.content)
    
gmx_checker("")