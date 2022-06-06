import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("dalyba.log")
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def division(x, y: int):
    try:
        dalyba = x / y
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        logger.info("%s skaiciaus dalyba is skaiciaus %s lygi %s" % (x, y, dalyba))
        return dalyba