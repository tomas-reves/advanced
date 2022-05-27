"""Sukurti antra_uzduotis.py failą ir jame parašyti klasę Person. Klasė Person turi būti parašyta taip, kad klasę importavus ir naudojant kitame faile ji veiktų šitaip:

from antra_uzduotis import Person

p = Person("Mantas", "Skara")
p.name = "Tomas"

print(p.fullname) # Tomas Skara
print(p.email()) # tomas.skara@gmail.com
p.fullname = "Juozas" # can't set attribute 'fullname'"""

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def email(self):
        return self.name + "." + self.surname + "@gmail.com"

    @property
    def fullname(self):
        return self.name + " " + self.surname