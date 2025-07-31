import imaplib
import email
import yaml
from datetime import datetime, timedelta

date = (datetime.now() - timedelta(days=0.5)).strftime("%d-%b-%Y")

with open("creds.yml") as f:
    content = f.read()

my_creds = yaml.load(content, Loader=yaml.FullLoader)

user, password = my_creds["user"], my_creds["password"]

imap = "imap.gmail.com"

my_mail = imaplib.IMAP4_SSL(imap)

my_mail.login(user, password)

my_mail.select("Inbox")

key = 'SINCE'
value = 'jobs-noreply@linkedin.com'
keywords = ['aliexpress', "application was sent to"]

_, data = my_mail.search(None, f'({key} {date})')

mail_id_list = data[0].split()

print(f"Found {len(mail_id_list)} emails since {date}")

msgs = []

_, mailboxes = my_mail.list()
print(mailboxes)

