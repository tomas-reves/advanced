"""Sukurti programą, kuri:
Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
Kitu atveju atspausdinti „Laimėjai!“
Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
"""
import random

listas = []
while len(listas) < 3:
    a = random.randint(1,6)
    listas.append(a)

if 5 in listas:
    print(listas)
    print("Lost")
else:
    print(listas)
    print("won")

