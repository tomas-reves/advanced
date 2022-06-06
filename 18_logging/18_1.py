"""Sukurti funkcijas, kurios:
Gražintų visų paduotų skaičių sumą (su *args argumentu)
Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
Gražintų paduoto sakinio simbolių kiekį (su len())
Gražintų rezultatą, skaičių x padalinus iš y

Nustatyti standartinį logerį (logging) taip, kad jis:
Saugotų pranešimus į norimą failą
Pranešimai turi būti tokiu formatu: data/laikas, logginimo lygis, žinutė

Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:
"""
import math
import logging

logging.basicConfig(level=logging.DEBUG, filename='log.log',
                    format="%(asctime)s:%(levelname)s:%(message)s")

def sum_of_args(*args: int):
    return sum(args)

def sqr_root_of_args(a: int):
    return math.sqrt(a)

def len_of_str(b: str):
    return len(b)

def division(x, y: int):
    return x / y

suma = sum_of_args(5,2,3)
squares = sqr_root_of_args("25")
length = len_of_str("Lskjaklfjslkdfjlsdkjflkasjdflk")
divide = division(999,3)


logging.info(f"suma: {suma}, skaičiaus šakisni: {squares}, eilutės ilgis: {length}, skaicius dalyba: {divide}")



