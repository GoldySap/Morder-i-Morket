from __future__ import annotations
import random
from typing import TYPE_CHECKING, List, Dict, Optional, Any

if TYPE_CHECKING:
    from location import Location

class SafeDict(dict):
    """Prevents crashing if an unknown placeholder variable is used in dialogue."""
    def __missing__(self, key):
        return f"{{{key}}}"

class NPC:
    """Superclass for characters with movement and conditional dialogue rules."""
    def __init__(self, name:str, role:str):
        self._name = name
        self._role = role
        self._is_dead = False
        self._is_killer = False
        self._location: Location | None = None
        self._dialogues: List[Dict[str, Any]] = []

    def get_name(self) -> str:
        return self._name

    def get_role(self) -> str:
        return self._role

    def is_alive(self) -> bool:
        return not self._is_dead

    def set_dead(self, status:bool = True):
        self._is_dead = status

    def set_killer(self, status:bool = True):
        self._is_killer = status

    def is_killer(self) -> bool:
        return self._is_killer

    def set_location(self, location:Location):
        self._location = location

    def get_location(self) -> Location | None:
        return self._location

    def add_dialogue(
        self, 
        topic: str, 
        response: str, 
        required_location: Optional[str] = None, 
        required_present: Optional[str] = None,
        required_night: Optional[int] = None
    ):
        """Allows defining custom dialogue with optional location, presence, and night conditions."""
        self._dialogues.append({
            "topic": topic.lower().strip(),
            "response": response,
            "required_location": required_location.lower().strip() if required_location else None,
            "required_present": required_present.lower().strip() if required_present else None,
            "required_night": required_night
        })

    def get_dialogues(self) -> List[Dict[str, Any]]:
        return self._dialogues

    def roam(self):
        """Allows the NPC to walk through connected doors into an adjacent room."""
        if self._is_dead or not self._location:
            return
        
        connections = self._location.get_connections()
        unlocked_connections = [room for room in connections.values() if not room.is_locked()]
        
        if unlocked_connections:
            target_room = random.choice(unlocked_connections)
            self._location.remove_npc(self)
            target_room.add_npc(self)

    def behavior(self):
        """Default behavior description for standard NPCs."""
        if self._is_dead:
            print(f"The cold body of {self._name} lies here.")
        else:
            print(f"{self._name} ({self._role}) is standing around.")

    def interact(
        self, 
        topic: str, 
        current_room: Location, 
        current_night: int, 
        killer_npc: NPC, 
        victim_npc: NPC, 
        player_name: str, 
        all_npcs: list[NPC]
    ):
        """Evaluates user-defined dialogue rules based on location, presence, and night internally."""
        if not self.is_alive():
            print(f"\n{self._name} is dead and cannot answer...")
            return

        topic_clean = topic.lower().strip()
        present_npcs = [other.get_name() for other in current_room.get_npcs() if other != self and other.is_alive()]
        current_room_name = current_room.get_name().lower()

        matched_response = None

        for rule in self._dialogues:
            if rule["topic"] == topic_clean:
                if rule["required_location"] and rule["required_location"] != current_room_name:
                    continue
                if rule["required_present"] and rule["required_present"].lower() not in [p.lower() for p in present_npcs]:
                    continue
                if rule["required_night"] is not None and rule["required_night"] != current_night:
                    continue
                
                matched_response = rule["response"]
                break

        if matched_response:
            context_data = {
                "player": player_name,
                "self": self._name,
                "npc": self._name,
                "name": self._name,
                "role": self._role,
                "killer": killer_npc.get_name(),
                "victim": victim_npc.get_name(),
                "room": current_room.get_name(),
                "location": current_room.get_name(),
                "present": ", ".join(present_npcs) if present_npcs else "anyone",
                "night": str(current_night),
            }

            for character in all_npcs:
                context_data[character.get_name().lower()] = character.get_name()
                context_data[character.get_role().lower()] = character.get_name()

            safe_context = SafeDict(context_data)
            formatted_text = matched_response.format_map(safe_context)

            print(f"\n{self._name} ({self._role}) says: \"{formatted_text}\"")
        else:
            print(f"\n{self._name} says: \"I don't know anything about the topic of: '{topic}'.\"")


class NervousSuspect(NPC):
    """Subclass representing a nervous character."""
    def behavior(self):
        if self._is_dead:
            print(f"The cold body of {self._name} lies here.")
        else:
            print(f"{self._name} ({self._role}) is sweating nervously, wringing their hands.")


class DefiantSuspect(NPC):
    """Subclass representing an aggressive/defensive character."""
    def behavior(self):
        if self._is_dead:
            print(f"The cold body of {self._name} lies here.")
        else:
            print(f"{self._name} ({self._role}) crosses their arms and avoids eye contact.")


class QuietSuspect(NPC):
    """Subclass representing a quiet/observant character."""
    def behavior(self):
        if self._is_dead:
            print(f"The cold body of {self._name} ({self._role}) lies here.")
        else:
            print(f"{self._name} ({self._role}) sits quietly in the shadows, observing everyone.")