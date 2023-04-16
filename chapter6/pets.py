pet1 = {
    'animal': 'dog',
    'owner': 'shankar'
}
pet2 = {
    'animal': 'cat',
    'owner': 'krishna'
}
pet3 = {
    'animal': 'dog',
    'owner': 'priyadharshan'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner'].title()} has a pet {pet['animal']}.")
