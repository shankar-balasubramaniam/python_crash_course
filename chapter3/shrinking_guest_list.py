dinner_invitees = ['Sowbarniga', 'Mugil', 'Priyadharshan']

print(f"Hey {dinner_invitees[0].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[1].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[2].title()}, let's have dinner tonight.")

print('\n')
absentee = 'Priyadharshan'
print(f"{absentee} can't make it to tonight's dinner.")

dinner_invitees.remove('Priyadharshan')
dinner_invitees.append('Madhuritha')

print('\n')
print(f"Hey {dinner_invitees[0].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[1].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[2].title()}, let's have dinner tonight.")

print('\n')
print('Hey guys, I got a bigger dinner table.')

dinner_invitees.insert(0, 'Dhanurs')
dinner_invitees.insert(2, 'Siva')
dinner_invitees.append('Thimmarayan')

print(f"Hey {dinner_invitees[0].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[1].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[2].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[3].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[4].title()}, let's have dinner tonight.")
print(f"Hey {dinner_invitees[5].title()}, let's have dinner tonight.")

print('\n')
print("I couldn't get the dinner table. Now I can only invite two of you.")

print('\n')

person1 = dinner_invitees.pop()
print(f"Sorry {person1}, I can't invite you to dinner.")

person2 = dinner_invitees.pop()
print(f"Sorry {person2}, I can't invite you to dinner.")

person3 = dinner_invitees.pop()
print(f"Sorry {person3}, I can't invite you to dinner.")

person4 = dinner_invitees.pop()
print(f"Sorry {person4}, I can't invite you to dinner.")

print('\n')
print(f"Hey {dinner_invitees[0].title()}, you are still invited.")
print(f"Hey {dinner_invitees[1].title()}, you are still invited.")

del dinner_invitees[0]
del dinner_invitees[0]

print(f'\n{dinner_invitees}')
