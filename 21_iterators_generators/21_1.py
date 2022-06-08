#Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next
# grąžintų sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos.

def every_second_numbers():
    count = 2
    while True:
        yield count
        count += 2

kas_du = every_second_numbers()
print(next(kas_du))
print(next(kas_du))
print(next(kas_du))
print(next(kas_du))
print(next(kas_du))
print(next(kas_du))
print(next(kas_du))

