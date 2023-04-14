current_users = ["shankar_b", "john_doe", "jane_smith",
                 "johndoe123", "janedoe456", "jsmith789"]

current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

new_users = ["janedoe456",
             "jsmith789",
             "johndoe789",
             "janesmith123",
             "johndoe456",
             "janedoe789"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Please enter a different username.")
    else:
        print("This username is available.")
