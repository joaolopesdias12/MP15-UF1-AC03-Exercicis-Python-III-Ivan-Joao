
from character import character
import json
from character_films import character_film

character_film_list = []
f = open("StarWars.json")

data = json.load(f)

for i in data:
    c = character.fromDict(i)
    print(c.name)

f.close()
