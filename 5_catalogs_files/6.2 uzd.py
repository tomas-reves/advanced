"""Sukurti programą, kuri:
Leistų vartotojui įvesti norimą eilučių kiekį (pvz. įvesti 5 ar 8 eilutes)
Pvz. vartotojas pasirenka įvesti du sakinius ir įveda “Python programavimo kalba” ir “JavaScript programavimo kalba”
Įrašytų įvestą tekstą atskiromis eilutėmis į failą (failas tegu būna sukuriamas tame pačiame kataloge kur dirbame)
Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
Išspausdintų failo turinį
Išspausdintų po vieną sakinį (nauja eilutė -  naujas sakinys, be tarpų tarp eilučių)
"""
pav = input("irasykite norima pavadinima ")
skaicius = int(input("iveskite norimu eiluciu skaiciu"))


for x in range(skaicius):
    naujas = input("Iveskite eilute: ")
    with open(f"{pav}.txt", 'a') as n:
        n.write(naujas + "\n")

with open(f"{pav}.txt", 'r') as f:
    print(f.read())

