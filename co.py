
import requests
import json
import re
from bs4 import BeautifulSoup
from verify_email import verify_email

def verify(email, ouputAlive = None):
	url = "https://mail.google.com/mail/gxlu?email={}".format(email)
	print(url)
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
	}
	resp_headers = requests.get(url=url, headers=headers).headers
	if "Set-Cookie" in resp_headers:
		if ouputAlive == 1:
			return "Alive"
		else:
			pass
	else:
		return "Unregistered"


# check = verify_email('HeatherLewis234@gmail.com')
check = verify('hikingadventures@gmail.com', 1)
print('GMAIL CHECKER : ', check)
