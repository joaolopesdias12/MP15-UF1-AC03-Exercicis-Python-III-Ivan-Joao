
from character import character
import json
from character_films import character_film

character_film_list = []

f = open("StarWars.json")
data = json.load(f)
f.close()

for i in data:
    c = character.fromDict(i["fields"])
    character_film_list.append(c)

for i, obj in enumerate(character_film_list):
    match obj.name :
        case "Anakin Skywalker":character_film_list[i] = character_film(obj, 7,"The Phantom Menace (Episode 1)", False)
        case "Luke Skywalker": character_film_list[i]= character_film(obj, 7,"Revenge of the Sith (Episode 3)", False)
        case "Chewbacca": character_film_list[i]= character_film(obj, 8,"Revenge of the Sith (Episode 3)", True)


map = map(lambda x: x.toDict(), character_film_list)


with open("list.json", 'w') as j:
    json.dump(list(map),j,  indent=4)

