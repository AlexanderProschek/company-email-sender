import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
from tqdm import tqdm
import sys

with open(str(sys.argv[1]), 'r') as file:
    for line in tqdm(file):
        company = re.search('@(.*)\.', line).group(1).title()

        message = Mail(
            from_email = str(os.environ.get('FROM_EMAIL')),
            to_emails = line,
            subject = str(os.environ.get('SUBJECT')),
            html_content = str(os.environ.get('CONTENT')) % (company, company))

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            tqdm.write(str(response.status_code))
            tqdm.write(str(response.body))
            tqdm.write(str(response.headers))
        except Exception as e:
            print(e.message)
            exit()