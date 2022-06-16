import requests
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
from string import Template

def send_mail(error):
    message = '''
    Dėmesio!

    Pranešame, kad negautas atsakas iš jūsų serverio. Klaidos žinutė tokia:

    $error
    '''
    sablonas = Template(message)

    email = EmailMessage()
    email['from'] = 'Vardas Pavardė'
    email['to'] = 'test.tomas4456@gmail.com'
    email['subject'] = 'email from python'

    email.set_content(sablonas.substitute({'error': e}), 'plain')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('test.tomas4456@gmail.com', 'ykchtioecvkflrgt')
        smtp.send_message(email)

    with open('server_error.txt', 'rb') as file:
        content = file.read()
        email.add_attachment(
            content,
            maintype='text/plain',
            subtype='plain',
            filename='server_error.txt')


while True:
    try:
        r = requests.get('http://localhost:8000')
        with open(f"server_log.txt", 'a') as n:
            n.write(f"{r.status_code} {datetime.today()}\n")
        st = r.status_code

        time.sleep(5)
    except Exception as e:
        with open('server_error.txt', 'a') as m:
            m.write(str(e))

        print(e)
        send_mail(e)
        break

