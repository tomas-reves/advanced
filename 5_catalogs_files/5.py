"""Sukurti programą, kuri:
Vienu lygiu žemiau darbinio katalogo sukurtų katalogą „Naujas Katalogas“ (pvz. jei dirbate direktorijoje Desktop -> CodeAcademy, tai sukurti aplanką Desktop vietoje)
Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data, laikas ir direktorija iki failo. Po laiko padaryti naują eilutę
Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais

Papildomai:
Sukurti katalogą/failą su savo norimu pavadinimu
Panaudoti try/catch kuriant tą patį katalogą
"""
import os
import datetime

time = datetime.datetime.now()


os.chdir("..")
if not os.path.isdir("CodeAcademy"):
    os.mkdir("CodeAcademy")

print(os.getcwd())

with open(os.path.join("CodeAcademy", "new.txt"), "w") as failas:
    failas.write(f"{time} {os.getcwd()} \n")

os.chdir("C:\\Users\\Acer\\Desktop\\python_kursai\\advanced\\CodeAcademy")

w








