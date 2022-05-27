"""Sukurti po vieną norimą sąrašą ir žodyną ir juose:
Atspausdinti vieną norimą įrašą (abiejuose)
Pridėti įrašą (abiejuose)
Ištrinti įrašą (abiejuose)
Ištrintą įrašą iš žodyno pridėti prie sąrašo (po antro elemento)
Sukurti naują sąrašą ir jam prilyginti jau prieš tai sukurtą (new_list = old_list)
Pakeiskite naujame saraše elementą ir išspausdinkite senąjį. Ar matote problemą?
Užkomentuokite senąjį kodą ir sutvarkykite prieš tai atrastą problemą
Jei senąjame sąraše tarp elementų būtų sąrašas/žodynas, ar jūsų kode problema vėl atsiranda? Jei atrandate problemą, sutvarkykite
"""

import copy

sarasas = [1, "Tomas", 58, "48", True, ["LT", "UA"]]
zodynas = {
    "Tomas":1.85,
    "Andrius":2.01,
    "Tadas":1.81,
    "Ieva":1.78
}
# print(sarasas[4])
# print(zodynas["Tomas"])

sarasas.append(100)
zodynas["Juste"] = 1.75
del sarasas[0]
del_dict_item = zodynas.pop("Tadas")
sarasas.insert(2, del_dict_item)

naujas_sarasas = copy.deepcopy(sarasas)
naujas_sarasas[5][0] = "T"
print(sarasas)
print(naujas_sarasas)

