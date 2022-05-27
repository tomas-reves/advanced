"""Sukurti programą, kuri:
Sukurtų duomenų bazę
Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)
Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
Ištrintų paskaitą, kurios dėstytojas – „Tomas“
Atspausdintų visas paskaitas (visą lentelę)
"""
import sqlite3

class Paskaitos:
    def __init__(self, subject, teacher, kreditai):
        self.subject = subject
        self.teacher = teacher
        self.kreditai = kreditai


    @property
    def kreditai(self):
        return self._kreditai

    @kreditai.setter
    def kreditai(self, value):
        if value > 0:
            self._kreditai = value
        else:
            self._kreditai = 20

    def print_info(self):
        print(f"{self.teacher}, {self.subject}, {self._kreditai}")
    # def create(self):
    #     conn = sqlite3.connect("paskaitos.db")
    #     p = conn.cursor()
    #     p.execute("CREATE TABLE IF NOT EXISTS paskaitos (subject text, teacher text, credits integer)")
    #     with conn:
    #         p.execute(f"INSERT INTO paskaitos VALUES ('{self.subject}', '{self.teacher}', '{self.credits}')")
    #
    # def display(self):
    #     conn = sqlite3.connect("paskaitos.db")
    #     p = conn.cursor()
    #     p.execute("SELECT * FROM paskaitos")
    #     p = p.fetchall()
    #     print(p)


# kursas = input("subject name ")
# dest = input("Lecture ")
# trukme = int(input("credits "))

destytojas = Paskaitos("Pitonas", "Tomas", -1)
destytojas.print_info()
# destytojas.create()
#
# destytojas.display()
