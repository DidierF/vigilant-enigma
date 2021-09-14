# Python 3.7
import json
import imaplib
import traceback

from parsers import parseBHDEmail

def getConfig():
    f = open('local.json')
    data = json.load(f)
    f.close()
    return data

def readEmail():
    config = getConfig()
    try:
        mail = imaplib.IMAP4_SSL(config.get('SMTP_SERVER'))
        mail.login(config.get('FROM_EMAIL'),config.get('FROM_PWD'))
        mail.select('inbox')

        # BHD
        _, ids_string = mail.search(None, 'FROM', '"alertas@bhdleon.com.do"')
        ids = ids_string[0].split()
        bhdData = []
        for id in ids:
            bhdData.append(parseBHDEmail(mail.fetch(id, '(RFC822)')))
        
        print(bhdData)

    except Exception as e:
            traceback.print_exc() 
            print(str(e))

readEmail()