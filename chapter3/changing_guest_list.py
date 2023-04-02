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
