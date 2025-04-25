from game_object import GameObject
from place import Place
from character import Character, Player, NPC
from item import Item
import os
import json


class GameEngine:
    def __init__(self):
        self.place_object_dict: dict[str, Place] = {}
        self.item_object_dict: dict[str, Item] = {}
        self.npc_object_dict: dict[str, Character] = {}
        self.player = None


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
            self.place_object_dict[name] = Place(name, description, takes_to)



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

            self.item_object_dict[name]  = Item(name, description, location, pickable)



    def assign_items_to_places(self):
        for key, item_object in self.item_object_dict.items():
            location = item_object.get_location()
            if location:
                self.place_object_dict[location].add_item(item_object)


    def load_characters(self):
        world = self.load_world()
        if world:
            characters = world['characters']
            for character in characters:
                name = character.get('name')
                description = character.get('description')
                location = character.get('location')
                character_type = character.get('type')
                self.npc_object_dict[name] = NPC(name, description, location, character_type)


    def create_player(self, name):
        player = Player(name)
        return player






game = GameEngine()
game.load_places()
game.load_items()
game.load_characters()

player = game.create_player('Turian')
Floresta = game.place_object_dict['Floresta']
player.go_to(Floresta)





# guerreiro = teste.npc_object_dict['Guerreiro']
# item = teste.item_object_dict['Armadura']

# vendo = teste.create_player()
# vendo.pick_up_item(item)
# vendo.drop_item(item)
# vendo.show_inventory(teste.item_object_dict)


