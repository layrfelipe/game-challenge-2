from game_object import GameObject
from place import Place
from item import Item
import os
import json


class GameEngine:
    def __init__(self):
        self.place_instance: dict[str, Place] = {}
        self.item_objects: dict[str, Item] = {}
        self.characters: list = []
        self.player = None
        self.item_locations: dict[str, str] = {}


    def find_world_path(self) -> str:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world.json')
    
    def load_world(self) -> dict:
        try:
            with open(self.find_world_path(), 'r', encoding='utf8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: The file 'worlds.json' was not found.")
        except PermissionError:
            print("Error: You do not have permission to access 'worlds.json'.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON — check the syntax in 'worlds.json'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def load_places(self):
        world = self.load_world()
        if not world:
            return

        locations = world.get("locations", [])
        for data in locations:
            name = data.get("name")
            description = data.get("description", "")
            takes_to = data.get("takes_to", [])
            place = Place(name, description, takes_to)
            self.place_instance[name] = place


    def load_items(self):
        world = self.load_world()
        if not world:
            return

        all_items_from_world = world.get("items", [])
        
        for data in all_items_from_world:
            name = data.get("name")
            description = data.get("description", "")
            location = data.get("location")
            pickable = data.get("pickable", False)

            price = data.get("price")
            offense_bonus = data.get("offense_bonus")
            defense_bonus = data.get("defense_bonus")
            usable = data.get("usable")

            item_object = Item(name, description, location, pickable)
            self.item_objects[name] = item_object


    def assign_items_to_places(self):
        for key, item_object in self.item_objects.items():
            location = item_object.get_location()
            if location:
                self.place_instance[location].add_item(item_object)





teste = GameEngine()
teste.load_places()
teste.load_items()

# print(teste.place_instance)
# print(teste.item_object)

for key, object in teste.item_objects.items():
    print(object.description)
