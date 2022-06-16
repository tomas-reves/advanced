import requests

def cat_photo(num):
    for i in range(num):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat{i}.jfif', 'wb') as f:
            f.write(r.content)

cat_photo(3)

