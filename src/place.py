from game_object import GameObject

class Place(GameObject):
    def __init__(self, place_name: str, place_description: str, place_takes_to: str):
        self.place = None
        self.place_description = place_description
        self.place_takes_to = None


    def describe(self):
        return self.place_description