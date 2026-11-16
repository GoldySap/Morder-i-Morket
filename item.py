class Item:
    """Class for items/clues in the game."""
    def __init__(self, name:str, description:str):
        self._name = name
        self._description = description

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description