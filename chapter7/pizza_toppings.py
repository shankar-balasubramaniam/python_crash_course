prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter 'quit' to stop adding toppings. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
