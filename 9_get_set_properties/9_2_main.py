from uzduotis import Person

p = Person("Mantas", "Skara")
p.name = "Tomas"

print(p.fullname) # Tomas Skara
print(p.email()) # tomas.skara@gmail.com
p.fullname = "Juozas" # can't set attribute 'fullname'


