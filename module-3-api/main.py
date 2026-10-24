import random
import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"

print("Pokemon Guessing Game!")
print("Guess the name of the Pokemon based on its height and weight.")

def pokemon(name):
    response = requests.get(API_URL + name.lower())
    if response.status_code == 200:
        data = response.json()
        height = data['height']
        weight = data['weight']
        return height, weight
    else:
        return None, None

print("height and weight of a random Pokemon:")
pokemon_list = ["pikachu", "bulbasaur", "charmander", "regigigas", "mewtwo", "rayquaza"]

input_pokemon = random.choice(pokemon_list)
height, weight = pokemon(input_pokemon)
if height is not None and weight is not None:
    print(f"Height: {height}, Weight: {weight}")
    for attempt in range(3):
        guess = input(f"Enter your guess for the Pokemon's name (attempt {attempt + 1}/3): ")
        if guess.lower() == input_pokemon:
            print("Correct! You guessed the Pokemon.")
            break
        print("Wrong guess.")
    else:
        print(f"The correct answer was {input_pokemon}.")


