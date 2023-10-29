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

headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}

email_list = []

def color(col):
	if col == 'yellow':
		return '\033[93m'
	if col == 'red':
		return '\033[91m'
	if col == 'green':
		return '\033[32m'
	if col == 'cyan':
		return '\033[36m'
	if col == 'magenta':
		return '\033[35m'
	if col == 'end':
		return '\033[0m'

mail_status = {'0': color('red')+'[-] Email is already use!'+color('end'), '1': color('green')+'[+] Email is available!  '+color('end')}

def yahoo_session():
	global acrumb, crumb, yahoo_cookie
	headers['X-Requested-With'] = 'XMLHttpRequest'
	sess_url = 'https://login.yahoo.com/account/module/create?specId=yidReg'
	response = requests.get(sess_url, timeout = 3, stream = False, verify = False)
	soup = BeautifulSoup(response.content, "html.parser")
	crumb = soup.find_all('input',{'name':'crumb'})[0].get('value')
	acrumb = soup.find_all('input',{'name':'acrumb'})[0].get('value')
	yahoo_cookie = response.cookies.get_dict()
	print("Cookie : ",yahoo_cookie)

def yahoo_check(email):
	global payload, req
	headers['X-Requested-With'] = 'XMLHttpRequest'
	headers['Content-Type'] = 'application/x-www-form-urlencoded'
	check_url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	payload = 'specId=yidreg&crumb='+crumb+'&acrumb='+acrumb+'&yid='+email
	req = requests.post(check_url, data = payload, timeout = 3, stream = False, verify = False, headers = headers, cookies = yahoo_cookie)
	status = req.content
	print("Status : ",status)
	if 'IDENTIFIER_EXISTS' in status:
		print(mail_status.get('0'), 'Domain: yahoo.com')
		email_list.append(email+'@yahoo.com')
	else:
		print(mail_status.get('1'), 'Domain: yahoo.com')
		
yahoo_session()
print(yahoo_check("ahmed@yahoo.com"))