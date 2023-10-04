import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}") # get pokeapi
    pokemon = response.json() # get all the info
    hp = pokemon['stats'][0]['base_stat']
    attacks = pokemon['moves']
    print("Name: " + str(pokemon['name']))
    print("ID: " + str(hp))
    print("ID: " + str(attacks))

if __name__ == "__main__":
    search_pokemon(sys.argv[1]) # get pokemon as argument in cli

