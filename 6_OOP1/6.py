"""You will be given an array of numbers.
For each number in the array you will need to create an object.
The object key will be the number, as a string. The value will be the corresponding character code, as a string.
Return an array of the resulting objects.
All inputs will be arrays of numbers. All character codes are valid lower case letters. The input array will not be empty."""

array = [118, 117, 120]

naujas = []

class Number():
    def __init__(self, sarasas):
        self.sarasas = sarasas

    def add_to_dictionary(self):
        listas = []
        for i in self.sarasas:
            listas.append({str(i):chr(i)})
        self.listas = listas

    def __str__(self):
        return self.listas

a = Number(array)
print(a)
a.add_to_dictionary()
print(a.listas)


#print(chr(70))

print(Number([118, 117, 120]) == [{'118': 'v'}, {'117': 'u'}, {'120': 'x'}])


