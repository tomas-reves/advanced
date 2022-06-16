from bs4 import BeautifulSoup
import requests
from random import shuffle

r = requests.get('https://www.delfi.lt/').text
bs = BeautifulSoup
soup = bs(r, 'html.parser')
head = soup.find_all('h3', class_='headline-title')

pirmas = []
antras = []
bad_words = ["Putinas", "Putinui", "Putiną"]

for x in head:
    headline_html = x.find('a', class_='CBarticleTitle')
    if not headline_html:
        continue
    for i in bad_words:
        tekstas1 = headline_html.text.strip()
        if i in tekstas1:
            continue

    tekstas = headline_html.text.strip()
    if ":" in tekstas:
        pirmas.append(tekstas.split(":")[0])
        antras.append(tekstas.split(":")[1])


shuffle(antras)
for i in range(len(pirmas)):
    print(pirmas[i], ":", antras[i])
