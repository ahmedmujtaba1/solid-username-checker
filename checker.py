import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def check_email_existence(email):
    if not is_valid_email(email):
        return "Invalid email address"

    domain = email.split('@')[1]

    smtp_servers = {
        'gmail.com': 'smtp.gmail.com',
        'yahoo.com': 'smtp.mail.yahoo.com',
        'hotmail.com': 'smtp.live.com',
    }

    if domain not in smtp_servers:
        return "SMTP server for this domain is not supported"

    try:
        server = smtplib.SMTP(smtp_servers[domain], 587)
        server.starttls()
        
        username = 'saadmohsinparoopia@gmail.com'
        password = 'ghzvtrbjgeeqynox'
        server.login(username, password)

        from_email = username
        to_email = email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Test Email'

        server.sendmail(from_email, to_email, msg.as_string())

        server.quit()

        return "Email exists"

    except smtplib.SMTPRecipientsRefused:
        return "Email does not exist"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    email_to_check = input("Enter an email address to check: ")
    result = check_email_existence(email_to_check)
    print(result)
