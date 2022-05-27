"""Parašyti programą, kuri:
Leistų vartotojui įvesti skaičių.
Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
Patarimas: Naudoti ciklą while, sąlygą if, break
"""

a = []
while True:
    sk = int(input("iveskite skaiciu "))
    if sk < 0:
        break
    a.append(sk)

print(sum(a))


