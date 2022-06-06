"""Perdaryti 2 užduoties programą (paeiliui), kad:
Dalybos funkcija būtų perkelta į dalyba.py modulį
dalyba.py faile iškviesti dalybos funkciją
Like veiksmai eina į aritmetika.py modulį
aritmetika.py faile importanti dalybą
Iškviesti artimetika modulį (python3 aritmetika.py)
Atlikus veiksmus surast problemą su logais (ar išsaugomi abu logai?)
Perrašyti logginga:
Kiekvienam modulį sukuriamas atskiras loggeris, kuris fiksuoja visus anksčiau aprašytus pranešimus
Skirtingi loggeriai ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje
Loge nurodyti logerio pavadinimą (su name)
Iškviesti artimetika modulį (python3 aritmetika.py)
Patikrinti ar dingo prieš tai minėta problema
"""

import dalyba
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

sqr_r = sqr_root_of_args(25)

divide = dalyba.division(10, 2)

logger.info(f"{sqr_r}, {divide}")
