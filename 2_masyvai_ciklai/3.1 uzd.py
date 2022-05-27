"""Sukurti programą, kuri:
Leistų vartotojui įvesti 5 žodžius
Pridėtų įvestus žodžius į sąrašą
Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index"""


listas = []
while len(listas) < 5:
    zodis = input("Iveskite zodi ")
    listas.append(zodis)

for i in listas:
    print(i, listas.index(i))

