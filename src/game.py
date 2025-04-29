from game_object import GameObject
from place import Place
import os
import json

class Game:
    def __init__(self, current_place):
        self.current_place = []



    def load_place(self):
        file_path = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(file_path, 'world.json')

        with open(json_path, 'r', encoding='utf8') as f:
            loading_worlds = json.load(f)

        locations = loading_worlds['locations']
        for place in locations:
            place_name = place.get('name')
            place_description = place.get('description')
            place_takes_to = place.get('takes_to')
            # print(place_name)
            # print(place_description)
            # print(place_takes_to)
            self.current_place.append(Place(place_name, place_description, place_takes_to))
            
    def show_description_test(self):
        to_see = self.current_place[2]
        vendo = to_see.describe()
        print(vendo)
