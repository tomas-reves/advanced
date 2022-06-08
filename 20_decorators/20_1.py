# Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)

from functools import wraps
from time import sleep
from typing import Callable


def sleep_decorator(laikas):
    def sleep_decorator(fn):
        def wrapper(*args):
            sleep(laikas)
            print(f"Funkcija buvo atidėta {laikas} sekundę(-es)")
            return fn(*args)
        return wrapper
    return sleep_decorator

def limit_args_decorator(args_count) -> Callable:
    def limit_args_decorator(func):
        def wrapper(*args):
            if len(args) > args_count:
                return "No more than 2 arguments are accepted"
            return func(args)
        return wrapper
    return limit_args_decorator


@limit_args_decorator(2)
@sleep_decorator(3)
def suma(*argss):
    return sum(*argss)


print(suma(1,2,3,59))