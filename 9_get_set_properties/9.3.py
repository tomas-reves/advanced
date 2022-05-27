"""Parašyti klasę "Student", kuri turėtų atributus “name” ir “credits”. Vardas gali būti bet koks, kreditų gali būti nuo 0 iki 30.
Parašyti klasei metodą, kuris išspausdina studento vardą ir kreditus. Metodas turėtų atlikti tik informacijos spausdinimą (jokios kitos logikos).

Vardas ir kreditai turi turėt galimybę būt priskiriami ir inicializacijos metu:
s = Studentas("Mantas", -5)

Jei kreditų priskiriama 0 ar mažiau(pvz -66), priskirti 0.
Jei kreditų priskiriama 30 ar daugiau(pvz 66), priskirti 30.
Panaudoti @property, @property.setter dekoratorius.
"""

class Student:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, new_credits):
        if new_credits < 0:
            self._credits = 0
        elif new_credits > 31:
            self._credits = 30
        else:
            self._credits = new_credits

    def student_info(self):
        print(f"{self.name}, {self.credits}")

s = Student("Mantas", 100)


s.student_info()





