# Sukurti programą, kuri:​
#
# Turėtų klasę Zmogus, su savybėmis vardas ir amzius​
#
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių​
#
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais​
#
# Įdėti sukurtus Zmogus objektus į naują sąrašą​
#
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)​
#
# ​
#
# Patarimai:​
#
# Naudoti sorted, attrgetter, reverse, funkciją repr​

from operator import attrgetter

class Zmogus:
    def __init__(self, num: int, vardas: str, amzius: int):
        self.num = num
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f"{self.num}, {self.vardas}, {self.amzius}"

zmogus1 = Zmogus(3, "Mantas", 26)
zmogus2 = Zmogus(2, "Justina", 18)
zmogus3 = Zmogus(1, "Viktorija", 35)

zmoniu_list = [zmogus1, zmogus2, zmogus3]

suriuositas = sorted(zmoniu_list, key=attrgetter("num"))
print(suriuositas)

amzius_sur = sorted(zmoniu_list, key=attrgetter("amzius"), reverse=True)
print(amzius_sur)