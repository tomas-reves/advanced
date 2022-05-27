"""Parašyti programą, kuri:
Apsirašytumėte du skirtingus sąrašus senas ir naujas
Naudojant for ciklą ir append užpildytumėte naują sąrašą dvigubai didesniomis reikšmėmis nei senąjame (pvz senas = [1,2], naujas = [2,4]
Tą patį padarytumėte su list comprehension (žiurėti Ciklai/Masyvai skaidres) (pvz element * 2 for element in a)
Panaudojant datetime palyginti šių dviejų technikų įvykdymo laiką. Kuris sąrašo užpildymas buvo greitesnis?

Antra dalis:
Lygiai tas pats kas viršuje, tik šįkart visiškai tuščią sąrašą užpildyti skaičiais nuo 0 iki 100000000
Vėl palygint for ciklo ir list comprehension veikimo laikus. Kas greičiau?"""
from datetime import datetime
import timeit

senas = [1,2]
naujas = []

start_time = datetime.now()
for i in senas:
    naujas.append(i*2)

end_time = datetime.now() - start_time
print(end_time)



start_time = datetime.now()
naujas_2 = [x*2 for x in senas]
print(naujas_2)


start_time = datetime.now()
listas = []
our_range = range(0,100000000)
# for i in our_range:
#     listas.append(i)
end_time = datetime.now() - start_time
print(end_time)

start_time = datetime.now()
new = [x for x in our_range]
end_time = datetime.now() - start_time
print(end_time)

