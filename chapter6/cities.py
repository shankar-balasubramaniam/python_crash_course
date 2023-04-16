cities = {
    'New York': {
        'country': 'United States',
        'population': 8_175_133,
        'fact': 'The Empire State Building has its own zip code.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13_515_271,
        'fact': 'Tokyo has the most Michelin-starred restaurants in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': 2_140_526,
        'fact': 'The Eiffel Tower was originally intended to be a temporary installation.'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fun fact: {info['fact']}")
    print()
