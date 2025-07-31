from imap_tools import MailBox
import yaml

with open("D:/gmail_reader/creds.yml") as f:
    content = f.read()

my_creds = yaml.load(content, Loader=yaml.FullLoader)

user, password = my_creds["user"], my_creds["password"]

emails_deleted = 0
uids_to_delete = []

keywords = ['aliexpress', 'tech expo', "application was sent to", "application was viewed", "unfortunately", "decided not to move forward", "decided to move forward with other candidates", 'noreply', 'no-reply', 'jobs', 'reducere', 'promotie', 'discount', 'sephora', 'carzz', 'bilete', 'greenpeace']
senders = [
    'jobs-noreply@linkedin.com', 'updates-noreply@linkedin.com',
    'ae-report-info05.a4@deals.aliexpress.com', 'ae-newsletter05.a0@deals.aliexpress.com',
    'jobalerts-noreply@linkedin.com', 'no-reply@accounts.google.com',
    'ae-news-interest04.a03@mail.aliexpress.com', 'transaction@notice.aliexpress.com',
    'security-noreply@linkedin.com', 'mark.ae.a7@mail.aliexpress.com'
]

with MailBox("imap.gmail.com").login(user, password) as mailbox:
    mailbox.folder.set("INBOX")
    for msg in mailbox.fetch(limit=3000):

        if any(kw in msg.subject.lower() or kw in msg.from_.lower() or kw in msg.text.lower() for kw in keywords) or msg.from_.lower() in senders:
            print("Matched:", msg.uid, msg.from_)
            uids_to_delete.append(msg.uid)

    if uids_to_delete:
        print("Deleting emails...")
        mailbox.move(uids_to_delete, "[Gmail]/Bin")
        emails_deleted += len(uids_to_delete)

    print(f"Total emails deleted: {emails_deleted}")

    
