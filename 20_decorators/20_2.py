#Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus.

def only_string_decorator(func):
    def wrapper(*args):
        for c in args:
            if type(c) != str:
                return "Only string arguments are allowed"
        return func(args)
    return wrapper

@only_string_decorator
def concantenate_words(*args):
    return "".join(*args)


print(concantenate_words("Labas", "Vakaras"))