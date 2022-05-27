class Kursas():
    def __init__(self, pavadinimas: str, destytojas: str, trukme_h: int):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme_h = trukme_h

    def destyti(self):
        print("Vyksta mokymas!")

    def __str__(self):
        return f"{self.pavadinimas}, {self.destytojas}, {self.trukme_h}"
