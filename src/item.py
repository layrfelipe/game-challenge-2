from game_object import GameObject
import os
import json
class Item(GameObject):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description)
        self.pickable = pickable
        self.location = location

    def examine(self):
        return self.description

    def use(self):
        # Default behavior — can be overridden by subclasses like Key or Consumable
        return "You can't use this item right now."

    def drop(self):
        return f"You dropped the {self.name}."

    def show(self):
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)


class Key(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable)

    def examine(self):
        return self.description

    def use(self):
        pass

    def drop(self):
        return f"You dropped the {self.name}."

    def show(self):
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)




     
# **PR 2:** Implementação da classe `Item` e subclasses simples.
#  Funcionalidade de `examinar item` e
# `olhar` (mostrando itens no lugar). Carregamento de itens do `mundo.json`.
    

# **`Item` (Herda de `ObjetoJogo`):**

# * Responsabilidades: Representar um objeto que pode ser examinado, pego, largado, etc.
# * Atributos: `nome`, `descricao`, `pegavel` (bool).
# * Métodos: `examinar()`.
# * **Subclasses (Exemplos):**
#   * `Chave`: Pode ter um atributo que identifica o que ela abre. Método `usar()`.
#   * `Consumivel`: Pode ter um efeito ao ser usado. Método `usar()`.