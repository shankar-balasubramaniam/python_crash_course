favorite_numbers = {
    'shankar': [30, 7],
    'sowbarniga': [7, 30],
    'siva': [6],
    'priyadharshan': [5],
    'krishna': [11]
}

# print(f"Shankar: {favorite_numbers['shankar']}")
# print(f"Sowbarniga: {favorite_numbers['sowbarniga']}")
# print(f"Krishna: {favorite_numbers['krishna']}")
# print(f"Siva: {favorite_numbers['siva']}")
# print(f"Priyadharshan: {favorite_numbers['priyadharshan']}")

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}:")
    for number in numbers:
        print(f"\t->{number}")
    print('\n')
