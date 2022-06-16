import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
#from slaptazodis import password # importuoju slaptažodį,
                                 # (galima nurodyti ir tiesiai į parametrus)

# elementarios email žinutės sukūrimas:
email = EmailMessage()
email['from'] = 'Vardas Pavardė'
email['to'] = 'test.tomas4456@gmail.com'
email['subject'] = 'email from python'

email.set_content('Sveiki adresate,\n\nČia yra laiško turinys\n\npagarbiai, siuntėjas')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
    smtp.starttls() # inicijuojame šifruotą kanalą
    smtp.login('test.tomas4456@gmail.com', 'ykchtioecvkflrgt') # nurodome prisijungimo duomenis
    smtp.send_message(email) # išsiunčiame žinutę