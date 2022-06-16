import requests
import json

def get_currencies():

    r = requests.get('http://api.frankfurter.app/latest')
    json_str = r.text
    result = json.loads(json_str)
    listas = []
    for key in result.keys():
        listas.append(key)
    return listas

def get_kursas(_from, to):
    param = {"from": _from, "to": to}
    r = requests.get('http://api.frankfurter.app/latest', params=param)
    f = json.loads(r.text)
    return f['rates']

print(get_kursas("RUB", "EUR"))