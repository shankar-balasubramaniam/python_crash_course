pizzas = ['veggie', 'margherita', 'pepperoni']

friend_pizzas = pizzas[:]

pizzas.append('non-veg loaded')

friend_pizzas.append('veg loaded')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
