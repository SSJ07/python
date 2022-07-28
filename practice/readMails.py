'''
    This program shows how to reads mail from your gmail account using python.

'''

import imaplib
import getpass

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)

mail.login("<your mail_id>", getpass.getpass())

mail.select("Inbox")

typ, data = mail.search(None, "SUBJECT", "Gmail")

for num in data:
    for n in num.split(" "):
        ty, data = mail.fetch(n, "(RFC822)")
        print data
