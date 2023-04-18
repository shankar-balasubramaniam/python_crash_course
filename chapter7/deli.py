sandwich_orders = ["BLT", "turkey and cheese", "ham and Swiss", "pastrami", "roast beef",
                   "grilled cheese", "vegetarian", "club", "tuna salad", "pastrami", "meatball sub", "pastrami"]
finished_sandwiches = []

pastrami = "pastrami"

print(f"This deli has run out of {pastrami}")

while pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami)

while sandwich_orders:
    current_sandwich_order = sandwich_orders.pop()
    print(f"I made your {current_sandwich_order} sandwich.")

    finished_sandwiches.append(current_sandwich_order)

print("\n")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} has been made.")
