from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from item import Item
    from npc import NPC

class Location:
    """Class for rooms in the house."""
    def __init__(self, name:str, description:str, is_locked:bool = False, required_key:str = None):
        self._name = name
        self._description = description
        self._is_locked = is_locked
        self._required_key = required_key
        self._connected_locations = {}
        self._items = []
        self._npcs = []

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def is_locked(self) -> bool:
        return self._is_locked

    def lock(self):
        self._is_locked = True

    def unlock(self):
        self._is_locked = False

    def get_required_key(self) -> str:
        return self._required_key

    def connect(self, direction:str, location:Location):
        self._connected_locations[direction.lower()] = location

    def get_connections(self) -> dict[str, Location]:
        return self._connected_locations

    def add_item(self, item: Item):
        self._items.append(item)

    def remove_item(self, item_name: str) -> Item | None:
        for item in self._items:
            if item.get_name().lower() == item_name.lower():
                self._items.remove(item)
                return item
        return None

    def get_items(self) -> list[Item]:
        return self._items

    def add_npc(self, npc: NPC):
        if npc not in self._npcs:
            self._npcs.append(npc)
            npc.set_location(self)

    def remove_npc(self, npc: NPC):
        if npc in self._npcs:
            self._npcs.remove(npc)

    def get_npcs(self) -> list[NPC]:
        return self._npcs