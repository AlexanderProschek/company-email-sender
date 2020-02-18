## Getting Started

Install all the python dependencies with `$ pip3 install -r ./requirements.txt`

---

## Scraping emails from Websites

To scrape emails from the [SaaS Mag Website](https://www.saasmag.com/saas-1000-2018/), run `$ python3 saasmagScraper.py` and the output will be split into `saasMag.csv` for all the real emails that were found and `genSaasmag.csv` for all the emails that were not found on the webistes, but just generated with common prefixes.

The same applies to scrape from [500.co](https://500.co/startups/), but run `$ python3 500coScraper.py` and emails will be saved into `500co.csv` and `gen500co.csv`.

---

## Sending emails to csv list of emails with SendGrid

To send the emails, take the `.env.samp` file and change its name to `.env` as well as fill in all the information in the blanks liek following:

```
export SENDGRID_API_KEY='123ABC'
export CONTENT='It's me'
export FROM_EMAIL='foo@bar.com'
export SUBJECT='Hello World'
```

Find the the SendGrid API key [here](https://app.sendgrid.com/guide/integrate/langs/python). Then run `$ source ./.env` and `$ python3 ./sender.py /path/to/emailFile.csv` and watch the emails get sent.
