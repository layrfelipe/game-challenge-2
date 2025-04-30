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
        self.world: dict[str] = {}
        self.player: Player = None
        self.current_place: Place = None


    def find_world_path(self) -> str:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world.json')
    

    
    def load_world(self) -> dict:
        try:
            with open(self.find_world_path(), 'r', encoding='utf8') as f:
                self.world = json.load(f)
                return self.world
                
        except FileNotFoundError:
            print("Error: The file 'worlds.json' was not found. Exiting the game...")
            
        except PermissionError:
            print("Error: You do not have permission to access 'worlds.json'. Exiting the game...")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON — check the syntax in 'worlds.json'. Exiting the game...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Exiting the game.")

        self.world = None
        return None


    def load_places(self):
        
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente, por isso, os locais não foram carregados.')
            
        locations = self.world.get("locations", [])
        if not locations:
            raise KeyError("Missing 'locations' key in world data.")
        
        for data in locations:
            name = data.get("name")
            description = data.get("description", "")
            takes_to = data.get("takes_to", [])
            self.place_object_dict[name] = Place(name, description, takes_to)




    def load_items(self):
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente, por isso, os itens não foram carregados.')

        all_items_from_world = self.world.get("items", [])
        if not all_items_from_world:
            raise KeyError("Missing 'items' key in world data.")
        
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
            if not location:
                raise ValueError(f"Item '{key}' does not have a defined location.")
            if location not in self.place_object_dict:
                raise KeyError(f"Location '{location}' for item '{key}' not found in place dictionary.")
            self.place_object_dict[location].add_item(item_object)



    def load_npcs(self):
        if not self.world:
            print('Mundo não foi carregado corretamente, por isso, os Personagens não foram carregados')
            return
        characters = self.world['characters']
        for character in characters:
            name = character.get('name')
            description = character.get('description')
            location = character.get('location')
            character_type = character.get('type')
            self.npc_object_dict[name] = NPC(name, description, location, character_type)
         


    def create_player(self, name):
        if not name:
            raise ValueError("Player name cannot be empty.")
        self.player = Player(name)
        return
    

    # def pick_up_item(self):
    #     self.player.pick_up_item(item_object)


    def show_inventory(self):
        self.player.show_inventory(self.item_object_dict)

    def defining_first_place(self):
        first_place_dic_key, first_place_object = next(iter(self.place_object_dict.items()))
        first_place_name = first_place_object.get_name()
        # print(first_place_name)
        self.current_place = first_place_object

    def show_go_to_places(self):
        print(f'Você está aqui: {self.current_place.name}')
        print('Você pode ir para:')
        places_to_go = self.current_place.get_takes_to()
        print(places_to_go)
        return places_to_go
        # for place in places_to_go:
        #     print(place)

    def change_places(self):
        self.show_go_to_places()
        user_input = input('para onde quer ir? ')
        if 'floresta' in user_input.lower() and 'floresta' in self.show_go_to_places():
            self.current_place = self.place_object_dict['Floresta']
        elif 'igreja' in user_input.lower() and 'igreja' in self.show_current_place_name():
            self.current_place = self.place_object_dict['Igreja']
        elif 'centro' in user_input.lower() or 'cidade' in user_input.lower():
            self.current_place = self.place_object_dict["Centro da cidade"]
        elif 'loja' in user_input.lower() or 'armaduras' in user_input.lower():
            self.current_place = self.place_object_dict["Loja de armaduras"]
        else:
            print('Por favor, escolha uma das opções')
    

    def show_current_place_name(self):
        print(self.current_place.name)

        

# **PR 4:** Implementação de `pegar`, `largar`, `inventario`.
# Implementação da movimentação simplificada (`ir <NomeDoLugar>`)
# e carregamento/uso das `conexoes` entre `Lugar`es.



game = GameEngine()
game.load_world()
game.load_places()
game.load_items()
game.load_npcs()

player = game.create_player('Turian')
# game.show_inventory()
game.defining_first_place()
# game.show_go_to_places()
game.change_places()
game.show_current_place_name()
# game.change_places()
# game.show_current_place_name()







