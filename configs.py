LOCATION_CONFIGS = {
    "Living Room": {
        "description": "A chaotic living room strewn with party decorations.",
        "exits": {"north": "Hallway"}
    },
    "Hallway": {
        "description": "A long, dimly lit hallway connecting the wing.",
        "exits": {"south": "Living Room", "down": "Basement", "east": "Bedroom", "west": "Kitchen"}
    },
    "Basement": {
        "description": "A dark basement. The air is heavy and cold.",
        "is_locked": True,
        "required_key": "Basement Key",
        "exits": {"up": "Hallway"}
    },
    "Bedroom": {
        "description": "A guest bedroom with an unmade bed.",
        "exits": {"west": "Hallway"}
    },
    "Kitchen": {
        "description": "A messy kitchen with dirty dishes stacked high.",
        "exits": {"east": "Hallway"}
    }
}

ITEM_CONFIGS = [
    {
        "name": "Basement Key",
        "description": "A heavy key marked 'Basement'.",
        "start_location": "Living Room"
    },
    {
        "name": "Torn Note",
        "description": "A note reading: 'Meet me downstairs after 1 AM.'",
        "start_location": "Bedroom"
    }
]

NPC_CONFIGS = [
    {
        "name": "Sam",
        "role": "Party Host",
        "type": "standard",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Look, {player}, {killer} has had a grudge against {victim} for weeks.",
                "required_night": 1
            }
        ]
    },
    {
        "name": "Jayson",
        "role": "Jock",
        "type": "standard",
        "dialogues": []
    },
    {
        "name": "Daniel",
        "role": "Heart Throb",
        "type": "standard",
        "dialogues": []
    },
    {
        "name": "Lorelei",
        "role": "Shy Nerd",
        "type": "standard",
        "dialogues": []
    },
    {
        "name": "Lamarr",
        "role": "DJ",
        "type": "nervous",
        "dialogues": [
            {
                "topic": "murder",
                "response": "On Night {night}, I was asleep! But I did hear {killer} walking around near the {room}.",
                "required_night": 1
            },
            {
                "topic": "murder",
                "response": "Now that it is Night {night}, I am getting really scared of {killer}.",
                "required_night": 2
            }
        ]
    },
    {
        "name": "Naomi",
        "role": "Mean Girl",
        "type": "defiant",
        "dialogues": [
            {
                "topic": "basement",
                "response": "Why are you asking me about this dark place, {player}? It gives me chills.",
                "required_location": "Basement"
            },
            {
                "topic": "sam",
                "response": "I won't say a word about {sam} while he is standing right here in the {room} with us!",
                "required_present": "Sam"
            }
        ]
    }
]