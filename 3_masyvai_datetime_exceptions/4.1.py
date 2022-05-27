"""Parašyti programą, kuri:
Leistų vartotojui įvesti sveiką skaičių .
Atspausdinti True, jei skaičius teigiamas ar neigiamas
Atspausdinti False, jei skaičius lygus 0 ir pabaigti programą
True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį skaicius_ne_nulis
Patarimas: naudoti input, boolean

Papildomai: Padaryti, kad programa sustotų įvedus netinkama simbolį (0.1, “f” ir t.t)"""

skaicius_ne_nulis = True

try:
    while skaicius_ne_nulis:
        skaicius = int(input("iveskite skaicius"))
        skaicius_ne_nulis = bool(skaicius)
        print(skaicius_ne_nulis)
        if not skaicius_ne_nulis:
            break
except ValueError:
    print("ivestas netinkamas simbolis")
