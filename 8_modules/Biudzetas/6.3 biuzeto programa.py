"""Patobulinti 5 pamokos biudžeto programą:

•Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
•Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
•Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
•Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
•Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą."""


class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f"{self.suma}"

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

class IslaiduIrasas(Irasas):
    def __init__(self, suma, isigyta_preke_paslauga, atsiskaitymo_budas):
        super().__init__(suma)
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.atsiskaitymo_budas = atsiskaitymo_budas

class Biudzetas(Irasas):
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, isigyta_preke_paslauga, atsiskaitymo_budas):
        islaidos = IslaiduIrasas(suma, isigyta_preke_paslauga, atsiskaitymo_budas)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas,PajamuIrasas):
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                suma += irasas.suma
        return f"{suma} EUR"

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos {irasas.suma} $, siuntejas: {irasas.siuntejas}, papildoma info: {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Islaidos: {irasas.suma} $, preke ar paslauga: {irasas.isigyta_preke_paslauga}, atsiskaitymo budas:{irasas.atsiskaitymo_budas}")



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