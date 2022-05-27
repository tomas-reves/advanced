"""
Sukurti žodyną kuris skirtas filtruoti darbuotojus ir parodyti jų algas
Raktui panaudoti vardą, pavardę
Išspausdinti tik darbuotojus kurių pavardė yra daugiau nei penki simboliai (len) ir jie uždirba daugiau nei 9000
Nenaudoti string karpymo funkcionalumo (pvz “John Parker”[5:11])
Išspausdinti tokiu formatu: Employees name is: John Parker, employee earns: 9999
Patalpinti gautas pavardęs į vieną iš duomenų struktūrų ir išspausdinti su for ciklu:
Išspausdinti tokiu formatu: If you have this surname, you have good salary: Parker
Pavardės neturi kartotis

Papildomai (nebūtina):
Leisti įvesti darbuotojų info (vardas, pavardė, alga) vartotojui (darbuotojų kiekį pasirenka pats programos naudotojas)
Kitos pradedančiųjų kurse išmoktos temos (pvz duomenų bazės)
"""
from sqlalchemy.orm import sessionmaker
import sqlite3
from model import engine, Darbuotojai


def add_record():
    Session = sessionmaker(bind=engine)
    s = Session()
    naujas = Darbuotojai(vardas, pavarde, atlyginimas)
    s.add(naujas)
    s.commit()

def query():
    conn = sqlite3.connect('darbuotojai.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Darbuotojai")
    records = c.fetchall()
    for r in records:
        print(f"{r[2]} {r[3]}, {r[4]} EUR")

def additional_query():
    conn = sqlite3.connect('darbuotojai.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Darbuotojai")
    records = c.fetchall()
    for r in records:
        if len(r[3]) > 5 and r[4] > 9000:
            print(f"{r[2]} {r[3]}, {r[4]} EUR")

def additional_query_2():
    darb_pavarde = []
    conn = sqlite3.connect('darbuotojai.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Darbuotojai")
    records = c.fetchall()
    for r in records:
        if len(r[3]) > 5 and r[4] > 9000:
            darb_pavarde.append(r[3])
    naujas = set(darb_pavarde)
    for i in naujas:
        print(f"If you have this surname, you have good salary: {i}.")

while True:
    menu = int(input("1 -- iveskite darbuotoja 2-- Perziureti darbuotojus 3-- perziureti darbuotojus, kuriu pavarde, "
                     "daugiau nei 6 simboliai, ir kurie uzdirba daugiau nei 2000 eur 4-- atspaudinti daugiausia "
                     "uzdirbanciu/-io darbuotojo pavarde  "))
    if menu == 1:
        vardas = input("Iveskite varda ")
        pavarde = input("Iveskite pavarde ")
        atlyginimas = int(input("Iveskite atlyginima "))
        add_record()
    elif menu == 2:
        query()
    elif menu == 3:
        additional_query()
    elif menu == 4:
        additional_query_2()
    else:
        exit()
