class GameObject:
    def __init__(self, place_name: str, place_description: str):
        self.name = place_name
        self.description = place_description


    def describe(self):
        return self.description