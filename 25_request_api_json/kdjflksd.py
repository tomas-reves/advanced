import requests
import json


r = requests.get('https://raw.githubusercontent.com/robotautas/kursas/master/requests/uzduotis.json')

print(r)