# person = {
#     'first_name': 'shankar',
#     'last_name': 'b',
#     'age': 25,
#     'city': 'coimbatore'
# }

# print(person['first_name'].title())
# print(person['last_name'].title())
# print(person['age'])
# print(person['city'].title())

person1 = {
    'first_name': 'shankar',
    'last_name': 'b',
    'age': 25,
    'city': 'coimbatore'
}

person2 = {
    'first_name': 'sowbarniga',
    'last_name': 's',
    'age': 24,
    'city': 'hamburg'
}

person3 = {
    'first_name': 'krishnaprasad',
    'last_name': 'b',
    'age': 23,
    'city': 'hosur'
}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and is from {person['city'].title()}.")
