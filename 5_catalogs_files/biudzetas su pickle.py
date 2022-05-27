"""Sukurti biudžeto programą, kuri:
Leistų vartotojui įvesti pajamas arba išlaidas. Pajamos įrašomos teigiamu skaičiumi, išlaidos neigiamu. Prirašyti pajamų ar išlaidų pavadinimą (pvz. Darbas: 1000, Žaidimai: -60)
Pajamas ir išlaidas saugotų žodyne, o žodyną pickle faile (uždarius programą, įvesti duomenys nedingtų)
Atvaizduotų jau įvestas pajamas ir išlaidas
Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
Išlaidos negalimos jei balansas tampa žemiau 0 (negalime eiti į skolą)
Parašyti atskiras funkcijas duomenų įrašymui, atvaizdavimui (galima ir saugojimui)

Papildomai:
Kas pasidarėte programą, galite pamėgint pasidaryti saugojimą su json
"""

import pickle

def add_to_journal(description, suma):

    try:
        with open('journal.pkl', 'rb') as pickle_in:
            journal_info = pickle.load(pickle_in)
        journal_info[description] = suma
        with open("journal.pkl", "wb") as pickle_out:
            pickle.dump(journal_info, pickle_out)
    except:
        journal_info = {}
        journal_info[description] = suma
        with open("journal.pkl", "wb") as pickle_out:
            pickle.dump(journal_info, pickle_out)

def income_entry():
    income_source = input("Enter source of income: ")
    suma = float(input("Enter income amount: "))
    if suma > 0:
        add_to_journal(income_source, suma)
    else:
        print("Income should be above 0, cannot be negative number")

def add_expenses():
    goods_services = input("Enter goods or services acquired: ")
    suma = float(input("Enter expenses amount: "))

    if suma < 0:
        if display_balance() + suma > 0:
            add_to_journal(goods_services, suma)
        else:
            print("Budget cannot be below zero, currently you cannot add additional expenses")
    else:
        print("Income should be below 0, cannot be positive number")

def show_budget_report():
    try:
        with open('journal.pkl', 'rb') as pickle_in:
            journal_info = pickle.load(pickle_in)
            print("Income/Expenses report:\n")
            for j, k in journal_info.items():
                print(f"{j} : {k} EUR")
    except:
        print("Error! Сannot display budget, nothing is entered in the budget!")

def display_balance():
    try:
        with open('journal.pkl', 'rb') as pickle_in:
            journal_info = pickle.load(pickle_in)
            balansas = 0
            for values in journal_info.values():
                balansas += values
            return balansas
    except:
        print("Error! Сannot display budget balance, nothing is entered in the budget!")


while True:

    choice = int(input("\n1 - Enter your income \n2 - Enter your expenses, \n3 - Display income/expenses report, \n4 - Display budget balance"
                       " \n9 - exit program ____________\n \n \n"))
    if choice == 1:
        income_entry()
    if choice == 2:
        add_expenses()
    if choice == 3:
        show_budget_report()
    if choice == 4:
        print(display_balance())
    if choice == 9:
        print("Good bye!")
        break

