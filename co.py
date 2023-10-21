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

# from verify_email import verify_email
# from email_validate import validate

email = "johnsmith@gmail.com".lower()
# print(validate(email))
import requests

r = requests.get(f"https://hunter.io/verify/rustomdeveloper@gmail.com", timeout=110)
print(r.content)