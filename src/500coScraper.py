#!python3

import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

# Prefixes in case script cannot find an email on companies website
prefixes = ['info', 'team', 'support', 'hello', 'sales', 'contact', 'help', 'marketing', 'social', 'business']

# Base URL to query the emails
url = 'https://companies.api.500.vc/api/v1/companies'

resp = requests.get(url, timeout=10)
respJSON = json.loads(resp.text)

# Go through each URL
for company in tqdm(respJSON['data']):

    compURL = re.sub('^ *http(|s)://(www\.|)', '', company['url'])
    compURL = re.sub('/.*$', '', compURL)

    tqdm.write(compURL)

    try:
        subRes = requests.get('http://' + compURL, timeout=10)
        subSoup = BeautifulSoup(subRes.text, 'html.parser')

        emails = []
        found = False
        for mailTo in subSoup.find_all('a'):
            if 'href' in mailTo.attrs and re.search('^mailto:', mailTo.attrs['href']):
                # Clean up email
                email = re.sub('^mailto:', '', mailTo.attrs['href'])
                email = re.sub('?.*$', '', email)
                email = email.trim()

                # Check if email valid-ish and not a duplicate
                if re.search('[^@]+@[^@]+\.[^@]+', email) and email not in emails:
                    tqdm.write("> " + email)
                    emails.append(email)
                    found = True

        if not found:
            for prefix in prefixes:
                emails.append(prefix + "@" + compURL)

        whereToSave = "gen500co.csv"
        if found:
            whereToSave = "500co.csv"

        with open(whereToSave, 'a') as file:
            for email in emails:
                file.write("%s\n" % email)
    except:
        pass