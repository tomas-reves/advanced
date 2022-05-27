"""Parašyti programą, kuri:
Paprašytų įvesti laiką toku formatu (2021-02-11)
Iš įvesto laiko atimtų 14 savaičių
Išspausdintų rezultata tokiu formatu (2020 - November - 05 - Thursday)
Jeigu data įvedama neteisingai išspausdinti:
Klaidą
Dabartinę datą tokiu formatu (2022 - May - 03 - Tuesday)
Patarimas: naudoti input, strptime, strftime"""
import datetime

while True:
    try:
        a = input("iveskite data formatu 2021-02-11")
        data = datetime.datetime.strptime(a, "%Y-%m-%d")
        nauja_data = data - datetime.timedelta(weeks=14)
        print(nauja_data.strftime("%Y - %B - %d - %A"))
    except:
        print("data ivesta neteisinga")