import random
import sys

from configs import NPC_CONFIGS, LOCATION_CONFIGS, ITEM_CONFIGS
from item import Item
from location import Location
from npc import NPC, DefiantSuspect, NervousSuspect, QuietSuspect, QuietSuspect
from player import Player


class MurderInTheDarkGame:
    def __init__(self):
        self._current_night = 1
        self._max_nights = 3
        self._actions_left_this_night = 3
        self._locations: dict[str, Location] = {}
        self._npcs: list[NPC] = []
        self._victim: NPC | None = None
        self._killer: NPC | None = None
        self._player: Player | None = None

    def get_actions_left(self):
        return self._actions_left_this_night

    def setup(self):
        """Builds the game world, items, characters, and player dynamically from configs."""
        self._setup_locations()
        self._setup_items()
        self._setup_characters()
        self._player = Player("Detective", self._locations["Living Room"])

    def _setup_locations(self):
        """Creates rooms and connections from LOCATION_CONFIGS."""
        for name, data in LOCATION_CONFIGS.items():
            loc = Location(
                name, 
                data["description"], 
                is_locked=data.get("is_locked", False), 
                required_key=data.get("required_key")
            )
            self._locations[name] = loc

        # Wire connections automatically
        for name, data in LOCATION_CONFIGS.items():
            current_loc = self._locations[name]
            for direction, target_name in data.get("exits", {}).items():
                if target_name in self._locations:
                    current_loc.connect(direction, self._locations[target_name])

    def _setup_items(self):
        """Creates and places items in rooms based on ITEM_CONFIGS."""
        for item_data in ITEM_CONFIGS:
            item = Item(item_data["name"], item_data["description"])
            target_room = item_data["start_location"]
            if target_room in self._locations:
                self._locations[target_room].add_item(item)

    def _setup_characters(self):
        """Instantiates NPCs, assigns dialogues, picks victim/killer, and scatters them."""
        created_npcs = []

        for conf in NPC_CONFIGS:
            npc_type = conf.get("type")
            if npc_type == "nervous":
                npc = NervousSuspect(conf["name"], conf["role"])
            elif npc_type == "defiant":
                npc = DefiantSuspect(conf["name"], conf["role"])
            elif npc_type == "quiet":
                npc = QuietSuspect(conf["name"], conf["role"])
            else:
                npc = NPC(conf["name"], conf["role"])

            # Register configured dialogues
            for d in conf.get("dialogues", []):
                npc.add_dialogue(
                    topic=d["topic"],
                    response=d["response"],
                    required_location=d.get("required_location"),
                    required_present=d.get("required_present"),
                    required_night=d.get("required_night")
                )
            created_npcs.append(npc)

        # Randomly select Victim and Killer
        self._victim = random.choice(created_npcs)
        created_npcs.remove(self._victim)
        self._victim.set_dead(True)

        self._killer = random.choice(created_npcs)
        self._killer.set_killer(True)

        self._npcs = [self._victim] + created_npcs

        # Scatter living NPCs across accessible rooms
        living_rooms = [loc for loc in self._locations.values() if loc.get_name() != "Basement"]
        for npc in created_npcs:
            random.choice(living_rooms).add_npc(npc)

        # Place victim's body in the basement
        self._locations["Basement"].add_npc(self._victim)

    def advance_time(self):
        """Advances turn, triggers NPC roaming, and checks night limits."""
        for npc in self._npcs:
            if npc.is_alive():
                npc.roam()

        self._actions_left_this_night -= 1
        if self._actions_left_this_night <= 0:
            self._current_night += 1
            self._actions_left_this_night = 3
            
            if self._current_night <= self._max_nights:
                print(f"\nNIGHT {self._current_night} HAS FALLEN...")
                print("The house grows darker. Time is running out to solve the case.")
            else:
                print("\nTHE FINAL MORNING HAS ARRIVED.")
                print("You have run out of time. You must make your final accusation now.")
                self._handle_accuse()

    def trigger_murder_game_over(self):
        """The game ends with a final accusation."""
        print("The investigation has ended.")

    def _handle_move(self, connections: dict) -> bool:
        direction = input(f"Direction to walk ({', '.join(connections.keys())}): ").strip().lower()
        return self._player.move(direction)

    def _handle_interrogate(self, npcs_in_room: list[NPC], current_room: Location) -> bool:
        if not npcs_in_room:
            print("\nThere is no one in this room.")
            return False

        print("\nWho do you want to interrogate?")
        for idx, npc in enumerate(npcs_in_room, 1):
            status = "(DEAD BODY)" if not npc.is_alive() else ""
            print(f" [{idx}] {npc.get_name()} {status}")

        try:
            npc_idx = int(input("Select person number: ")) - 1
            target_npc = npcs_in_room[npc_idx]
            
            if not target_npc.is_alive():
                print(f"\n{target_npc.get_name()} is dead and cannot speak.")
                return False

            dialogues = target_npc.get_dialogues()
            if not dialogues:
                print(f"\n{target_npc.get_name()} has nothing to say right now.")
                return False

            print("\nWhat do you want to ask about?")
            topic_options = {}
            valid_rooms = {room.lower(): room for room in LOCATION_CONFIGS.keys()}
            current_room_name = current_room.get_name()
            current_room_lower = current_room_name.lower()

            idx = 1
            for rule in dialogues:
                topic_name = rule.get('topic', '').lower()

                if topic_name in topic_options.values():
                    continue

                if topic_name in valid_rooms:
                    if topic_name == current_room_lower:
                        display_name = f"This room ({current_room_name})"
                        topic_options[str(idx)] = topic_name
                        print(f" [{idx}] {display_name}")
                        idx += 1
                else:
                    display_name = topic_name.replace('_', ' ').title()
                    topic_options[str(idx)] = topic_name
                    print(f" [{idx}] {display_name}")
                    idx += 1

            if not topic_options:
                print(f"\n{target_npc.get_name()} has no topics to discuss with you in this room.")
                return False

            topic_choice = input(f"Choose topic (1-{len(topic_options)}): ").strip()
            topic = topic_options.get(topic_choice)

            if topic is None:
                print("\nInvalid topic choice.")
                return False

            target_npc.interact(
                topic,
                current_room,
                self._current_night,
                self._killer,
                self._victim,
                self._player.get_name(),
                self._npcs
            )
            return True
        except (ValueError, IndexError):
            print("\nInvalid choice.")
            return False

    def _handle_accuse(self):
        print(" ACCUSATION ROOM: MAKE YOUR CLAIM ")
        living_suspects = [npc for npc in self._npcs if npc.is_alive()]
        
        for idx, suspect in enumerate(living_suspects, 1):
            print(f" [{idx}] {suspect.get_name()} ({suspect.get_role()})")

        try:
            accuse_idx = int(input("\nSelect the killer's number: ")) - 1
            chosen_suspect = living_suspects[accuse_idx]

            print(f"\nYou gather everyone and accuse {chosen_suspect.get_name()} of murder!")

            if chosen_suspect == self._killer:
                print("\nVICTORY! YOU FOUND THE KILLER!")
                print(f"{chosen_suspect.get_name()} breaks down and admits to killing {self._victim.get_name()}!")
                print("You successfully solved the mystery before time ran out!")
            else:
                print("\nWRONG ACCUSATION!")
                print(f"{chosen_suspect.get_name()} is innocent!")
                print(f"The real killer was {self._killer.get_name()}! They strike you down in the chaos!")

            sys.exit()
        except (ValueError, IndexError):
            print("\nInvalid selection.")

    def play(self):
        self.setup()

        print("MURDER IN THE DARK ")
        print("Six people were stuck in this house last night.")
        print("Morning came, and one person was found dead!")
        print(f"You have {self._max_nights} nights to uncover who among the survivors is the killer.\n")
        print(f"Initial Report: {self._victim.get_name()} ({self._victim.get_role()}) was killed on night one!")

        while True:
            current_room = self._player.get_current_location()

            print("\n--------------------------------------------------")
            print(f"NIGHT: {self._current_night}/{self._max_nights} | ACTIONS REMAINING THIS NIGHT: {self._actions_left_this_night}")
            print(f"LOCATION: {current_room.get_name()}")
            print(f"DESCRIPTION: {current_room.get_description()}")

            connections = current_room.get_connections()
            print(f"EXITS: {', '.join(connections.keys()).upper()}")

            items_in_room = current_room.get_items()
            if items_in_room:
                print("ITEMS IN ROOM:")
                for item in items_in_room:
                    print(f"  - {item.get_name()}")

            npcs_in_room = current_room.get_npcs()
            if npcs_in_room:
                print("PEOPLE PRESENT:")
                for npc in npcs_in_room:
                    npc.behavior()

            print("\nACTION MENU:")
            print(" [1] Move to another room")
            print(" [2] Pick up an item")
            print(" [3] Interrogate someone (Consumes 1 Action & NPCs move)")
            print(" [4] View Inventory")
            print(" [5] ACCUSE THE KILLER (Final Decision)")
            print(" [6] Quit Game")

            choice = input("\nSelect choice (1-6): ").strip()

            if choice == "1":
                self._handle_move(connections)
                

            elif choice == "2":
                if not items_in_room:
                    print("\nThere are no items to pick up.")
                else:
                    item_name = input("Enter item name: ").strip()
                    self._player.pick_up_item(item_name)

            elif choice == "3":
                if self._handle_interrogate(npcs_in_room, current_room):
                    self.advance_time()

            elif choice == "4":
                self._player.show_inventory()

            elif choice == "5":
                self._handle_accuse()

            elif choice == "6":
                print("\nAbandoning the investigation. Goodbye!")
                break


if __name__ == "__main__":
    game = MurderInTheDarkGame()
    game.play()