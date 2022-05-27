"""Perrašyti kurso datų programą naudojant objektinį programavimą.
Leisti įvesti kurso datą, bet tik nuo 2022 metų. Jei įvesti ankstesni metai, tai išprintinti, kad keičiami metai į 2022 ir į juos perkelti. Diena ir mėnuo lieka tie patys.
Kursų gali būti įvairių, su skirtingais pavadinimais, paskaitų skaičiumi ir paskaitos valandomis (pvz. 2h, o ne 4h)
Galimybė pridėti atšauktų dienų list per atributą.

PAPILDOMAI:
Padarykite, kad nebūtų galima atšaukti dienų Lapkritį (property, setter)
"""
import datetime

class Course:
    def __init__(self, name, total_hours, lesson_length, start_date, cancelled_dates = []):
        self.name = name
        self.total_hours = total_hours
        self.lesson_length = lesson_length
        self.start_date = start_date
        self.cancelled_dates = cancelled_dates
        self.__moving_date = start_date

    @property
    def days_count(self):
        return int(self.total_hours / self.lesson_length)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if value < datetime.date(2022, 1, 1):
            self._start_date = datetime.date(2022, value.month, value.day)
        else:
            self._start_date = value

    def calculate(self):
        course_date_list = []
        while len(course_date_list) < self.days_count:
            weekday = self.__moving_date.isoweekday()
            if weekday in (1, 2, 3, 4):
                if self.__moving_date in self.cancelled_dates:
                    self.__moving_date = self.__moving_date + datetime.timedelta(days=1)
                else:
                    course_date_list.append(self.__moving_date)
                    self.__moving_date = self.__moving_date + datetime.timedelta(days=1)
            else:
                self.__moving_date = self.__moving_date + datetime.timedelta(days=3)
        return course_date_list

    def print_date(self):
        for day in self.calculate():
            print(day.strftime("%Y - %B - %d"))

    def print_info(self):
        self.print_date()
        prit(f"Kurso pavadinimas {self.name}, jo ilgis yra {self.days_count} dienos.")

cancelled_dates = [datetime.date(2022, 5, 4), datetime.date(2022, 5, 11),
                       datetime.date(2022, 7, 6), datetime.date(2022, 8, 15),
                       datetime.date(2022, 11, 1), datetime.date(2022, 11, 2)]

c = Course("Python", 25, 5, datetime.date(2000,4,28), cancelled_dates)
c.print_date()