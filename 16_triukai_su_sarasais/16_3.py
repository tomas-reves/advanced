sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras", True, False]

a = sum(x for x in sarasas if type(x) is int or type(x) is float)
print(a)

b = " ".join([x for x in sarasas if type(x) is str])
print(b)

c = [x for x in sarasas if x is True]
print(len(c))