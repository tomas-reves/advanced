from darbuotojas import Darbuotojas, engine
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_record():
    name = input("Name ")
    surname = input("Surname ")
    birth_date = input("Date of birth ")
    position = input("Position ")
    salary = input("Salary ")
    start_date = input("Start date ")
    employee = Darbuotojas(name, surname, birth_date, position, salary, start_date)
    session.add(employee)
    session.commit()

def update_record():
    get_id = int(input("Enter ID of employee to be updated: "))
    change = int(input("Enter 1 -- update name\nEnter 2 -- update surname\nEnter 3 -- update date of birth\n"
                       "Enter 4 -- update position\nEnter 5 -- update salary\nEnter 6 -- update start date\n"))
    employee = session.query(Darbuotojas).get(get_id)
    if change == 1:
        employee.name = input("Enter new name ")
    if change == 2:
        employee.surname = input("Enter new surname ")
    if change == 3:
        employee.birth_date = input("Enter new date of birth ")
    if change == 4:
        employee.position = input("Enter new position ")
    if change == 5:
        employee.salary = input("Enter new salary ")
    if change == 6:
        employee.start_date = input("Enter new start of date ")
    session.commit()

def delete_record():
    get_id = int(input("Enter ID of employee to be deleted: "))
    employee = session.query(Darbuotojas).get(get_id)
    session.delete(employee)
    session.commit()

def get_all_records_list():
    conn = sqlite3.connect('darbuotojas.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Darbuotojas")
    records = c.fetchall()
    for r in records:
        print(f"{r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}, {r[6]}")

while True:
    choice = int(input("1 -- add record \n"
                       "2 -- update record \n"
                       "3 -- delete record \n"
                       "4 -- display \n "
                       "5 -- exit \n"))

    if choice == 1:
        add_record()
    if choice == 2:
        update_record()
    if choice == 3:
        delete_record()
    if choice == 4:
        print(get_all_records_list())
    if choice == 5:
        break