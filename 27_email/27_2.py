import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
#from slaptazodis import password # importuoju slaptažodį,
                                 # (galima nurodyti ir tiesiai į parametrus)


def skolos_email(vardas: str, emailas: str, skola: float):
# elementarios email žinutės sukūrimas:
    email = EmailMessage()
    email['from'] = 'Skolų išieškojimo įmonė'
    email['to'] = emailas
    email['subject'] = 'dėl Jūsų skolos'

    email.set_content(f'Gerbiamas {vardas},\n\nInformuojame, kad vis dar nesate grąžinęs įsiskolinimo: {skola} EUR \n\npagarbiai, Skolų išieškojimo įmonė')

    with open('logo.JPG', 'rb') as file:
        content = file.read()
        email.add_attachment(
            content,
            maintype='image/jpg',
            subtype='jpg',
            filename='logo.jpg')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
        smtp.starttls() # inicijuojame šifruotą kanalą
        smtp.login('test.tomas4456@gmail.com', 'ykchtioecvkflrgt') # nurodome prisijungimo duomenis
        smtp.send_message(email) # išsiunčiame žinutę


skolos_email("Andrius", 'test.tomas4456@gmail.com', 1000.0)