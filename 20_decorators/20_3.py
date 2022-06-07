"""Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti.
Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais
vykdymo laikas - XX s. Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą
ir su funkcija, išrenkančia pirminius skaičius užduotame diapazone."""

import requests
from time import time

def function_time_count_decorator(func):
    def wrapper(args):
        start_time = time()
        func(args)
        end_time = time()
        result = end_time - start_time
        print(f"Funckijos {func.__name__} su {args} vykdymas laikas {result}")
    return wrapper

@function_time_count_decorator
def request_website(website: str):
    r = requests.get(website)  # sukuriame http užklausą
    print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)


request_website('https://www.delfi.lt/')


