import json

# a = {
#     'name' : 'Tomas',
#     'age': 2,
#     'height' : 182
# }
#
# data = json.dumps(a)
# with open('test.json', 'w') as f:
#     f.write(data)
#     f.close()

myRecord = json.load(open('test.json'))
print(myRecord)