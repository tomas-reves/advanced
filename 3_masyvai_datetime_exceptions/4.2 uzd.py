"""Parašyti programą, kuri:
Atspausdintų dabartinę datą ir laiką
Atimtų iš dabartinės datos ir laiko 5 dienas ir atspausdintų
Pridėti prie dabartinės datos ir laiko 8 valandas ir atspausdintų
Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
Patarimas: naudoti datetime, timedelta

Papildomai: papildomi aritmetiniai veiksmai su data"""

import datetime

date_now = datetime.datetime.now()
delta_time_5 = datetime.timedelta(days=5)
delta_time_8_hours = datetime.timedelta(hours=8)
pakeista_data = date_now - delta_time_5
pakeista_data_2 = date_now + delta_time_8_hours



print(pakeista_data)
print(pakeista_data_2)
print(date_now.strftime("%Y %m %d %X"))


