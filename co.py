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
k

print(validate_or_fail("rustomdeveloper@gmail.com",check_dns=False, check_smtp=False, check_format=False, check_blacklist=True))

# email = "johnsmith@gmail.com".lower()
# # print(validate(email))
# import requests, json

# formdata1 = {
#     "emails" : "khizranmohsi22n%40gmail.com",
# }

# formdata = json.dumps(formdata1)

# r = requests.post("https://www.site24x7.com/tools/email-validator", data=formdata)
# print(r.content)