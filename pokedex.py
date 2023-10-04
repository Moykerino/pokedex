import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}") # get pokeapi
    pokemon = response.json() # get all the info
    print("Name: " + str(pokemon['name']))
    print("ID: " + str(pokemon['id']))
    print("Base XP: ", str(pokemon['base_experience']))

if __name__ == "__main__":
    search_pokemon(sys.argv[1]) # get pokemon as argument in cli

