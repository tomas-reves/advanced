"""Sukurti programą, kuri:
Turėtų klasę Darbuotojas
Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
Sukurti norimą Darbuotojo objektą
Sukurti norimą NormalusDarbuotojas objektą
Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
"""

from datetime import datetime

class Employee:
    def __init__(self, name: str, hourly_pay: int, works_since: str):
        self.name = name
        self.hourly_pay = hourly_pay
        self.works_since = works_since

    def _days_count(self):
        start_date = datetime.strptime(self.works_since, "%Y-%m-%d")
        dienu_sk = datetime.now() - start_date
        final_days = dienu_sk.days
        return final_days


    def calculate_salary(self):
        salary = int(self._days_count())*8*self.hourly_pay
        return salary

    def __str__(self):
        return f"{self.name}, earns {self.hourly_pay} per hour, works since {self.works_since}"

class NormalEmployee(Employee):

    def calculate_salary(self):
        super().calculate_salary()
        salary = int(self._days_count())/7*5*8*self.hourly_pay
        return salary

Tadas = Employee("Tadas", 10, '2022-05-01')
print(Tadas)

print(Tadas.calculate_salary())

Marius = NormalEmployee("Marius", 10, '2022-05-01')
print(Marius.calculate_salary())