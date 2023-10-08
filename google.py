from validate_email_address import validate_email

def check_email_existence(email):
    is_valid = validate_email(email, verify=True)

    if is_valid:
        print(f'The email address "{email}" is valid and may exist.')
    else:
        print(f'The email address "{email}" is not valid or may not exist.')

# email_address = 'ahmed@hotmail.com'  
# check_email_existence(email_address)
