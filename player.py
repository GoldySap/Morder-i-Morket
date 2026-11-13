from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from location import Location
    from item import Item

class Player:
    """Class handling player state, inventory, and movement."""
    def __init__(self, name: str, start_location: Location):
        self._name = name
        self._current_location = start_location
        self._inventory: list[Item] = []

    def get_name(self) -> str:
        return self._name

    def get_current_location(self) -> Location:
        return self._current_location

    def has_item(self, item_name: str) -> bool:
        return any(item.get_name().lower() == item_name.lower() for item in self._inventory)

    def move(self, direction: str) -> bool:
        direction = direction.lower()
        connections = self._current_location.get_connections()

        if direction not in connections:
            print("\nYou cannot go that way.")
            return False

        target_room = connections[direction]

        if target_room.is_locked():
            required_key = target_room.get_required_key()
            has_key = any(item.get_name().lower() == required_key.lower() for item in self._inventory)

            if has_key:
                print(f"\nYou use '{required_key}' to unlock {target_room.get_name()}!")
                target_room.unlock()
                self._current_location = target_room
                print(f"You entered {target_room.get_name()}.")
                return True
            else:
                print(f"\nThe door to {target_room.get_name()} is locked! You need: {required_key}.")
                return False
        else:
            self._current_location = target_room
            print(f"\nYou walked to {target_room.get_name()}.")
            return True

    def pick_up_item(self, item_name: str):
        item = self._current_location.remove_item(item_name)
        if item:
            self._inventory.append(item)
            print(f"\nYou picked up: {item.get_name()}.")
        else:
            print(f"\nNo item named '{item_name}' found here.")

    def show_inventory(self):
        print("\nINVENTORY")
        if not self._inventory:
            print("Your inventory is empty.")
        else:
            for item in self._inventory:
                print(f"- {item.get_name()}: {item.get_description()}")