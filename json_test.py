import json

data = json.load(open('people.json'))

print(data['people'][0]['firstName'])

for person in data['people']:
    print(f'{person["firstName"]}', end="")
    print(f' {person["lastName"]} ', end="")
    print('is a famous Computer Scientist.', end="")
    print("")
