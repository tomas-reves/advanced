"""Perdaryti 1 užduoties programą, kad:
Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu

Patarimas: panaudoti try/except/else, logging.exception()"""

import math
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("veiksmai.log")
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def sqr_root_of_args(a: int):
    try:
        saknis = math.sqrt(a)
    except TypeError:
        logger.exception("Netinkamas formatas")
    else:
        logger.info("skaiciaus %s saknis %s" % (a, saknis))
        return saknis

def sum_of_args(*args: int):
    return sum(args)

def len_of_str(b: str):
    return len(b)

def division(x, y: int):
    try:
        dalyba = x / y
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        logger.info("%s skaiciaus dalyba is skaiciaus %s lygi %s" % (x, y, dalyba))
        return dalyba

sqr_r = sqr_root_of_args(25)

divide = division(10, 2)


logger.info(f"{sqr_r}, {divide}")
