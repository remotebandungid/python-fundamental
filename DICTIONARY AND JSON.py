# DICTIONARY

dict = {
    'id': 1,
    'name': 'Prayudha octavio',
    'username': 'aphr0',
    'email': 'Aphro@gmail.com',
}

print(dict)
print(dict['id'])
print(dict['name'])
print(dict['username'])
print(dict['email'])

# DICTIONARY DIDALAM DICTIONARY

database = {
    'id': 1,
    'name': 'Prayudha octavio',
    'username': 'aphr0',
    'email': 'Aphro@gmail.com',
    'address': {
        'street': 'jl. boscha no. 4',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1546'
        }
    }
}

print(database)
print(database['address']['geo']['lat'])

# JSON SAMA DENGAN DICTIONARY PADA PYTHON YANG AKAN DIGUNAKAN UNTUK MENYIMPAN DATABASE
# NAMUN JSON HARUS DI IMPORT TERLEBIH DAHULU DENGAN :

import json
result = json.dumps(database)
# berbentuk string karna json.dumps


with open('result.json', 'w') as file:
    json.dump(database, file)

# string diatas dapat membuat file baru bernama result yang isinya berbentuk format json