favorite_places = {
    'Alice': ['Central Park', 'The Met', 'Brooklyn Bridge'],
    'Bob': ['Grand Canyon', 'Yellowstone National Park'],
    'Charlie': ['Eiffel Tower', 'The Louvre']
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()
