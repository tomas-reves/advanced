import requests

"""Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų ir atspausdintų oro prognozę Vilniuje šiuo metu. Galima naudoti str metodus, regex."""

r = requests.get('https://orai.15min.lt/prognoze/vilnius')
h = r.content

print(h)
