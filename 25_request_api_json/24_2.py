import requests

listas = ['https://www.delfi.lt/', 'https://www.alfa.lt/', 'https://www.15min.lt/', 'https://www.lrytas.lt/', 'http://www.google.com/']

def get_servers(ls: list):
    for i in listas:
        r = requests.get(i)
        print(f"{i} {r.headers['Server']}")


get_servers(listas)


