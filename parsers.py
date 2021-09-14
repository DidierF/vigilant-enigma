import email

from bs4 import BeautifulSoup as bs

def parseBHDEmail(data):
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_bytes(arr[1])
            if msg.is_multipart():
                for part in msg.walk():    
                    if part.get_content_type() == 'text/html':
                        x = part.get_payload(None, True)
                        soup = bs(x, 'html.parser')
                        data = soup.body.html.body.find_all('table')[1].tbody.tr.find_all('td')
                        row = {
                            'date': data[0].string,
                            'cost': data[2].string,
                            'store': data[3].string,
                        }
                        return row