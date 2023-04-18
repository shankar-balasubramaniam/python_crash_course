prompt = "\nEnter your age:"
prompt += "\n(Enter 'quit' to exit) "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        ticket_price = 0
        print("The ticket is free.")
        continue
    elif age < 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"The ticket price is ${ticket_price}")
