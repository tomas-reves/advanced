from modules.biudzetas import *

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - ivesti islaidas, \n3 - gauti balansa, \n4 - parodyti ataskaita, \n9 - iseiti iš programos ____________"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamu sumą: "))
        siuntejas = input("iveskite siunteja: ")
        extra_info = input("iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, extra_info)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        preke_paslauga = input("Iveskite preke arba paslauga: ")
        atsis_budas = input("Iveskite atsiskaitymo buda: ")
        biudzetas.prideti_islaidu_irasa(suma, preke_paslauga, atsis_budas)
    if pasirinkimas == 3:
        print(biudzetas.gauti_balansa())
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break