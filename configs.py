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
    },

    {
    "name": "Party Log",
    "description": (
        "A crumpled paper recording events from the party. "
        "12:40 AM - Someone spilled a drink in the kitchen. "
        "12:55 AM - {killer} borrowed a flashlight. "
        "1:10 AM - A loud noise was heard downstairs. "
        "The rest of the paper is torn off."
    ),
    "start_location": "Kitchen"
},




]

NPC_CONFIGS = [
    {
        "name": "Sam",
        "role": "Party Host",
        "type": "calm",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Wait... someone actually died? Dude, I literally just wanted to throw a party. This is NOT what I had planned for tonight.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "Honestly? I don't know. Everyone was acting weird last night. But if I had to guess, I'd say {suspect}. They seem to know more than they let on. No offense.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "don’t ask me what makes you think I know??",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Oh hey! Just looking for something to eat. I swear there's never enough food in this house.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "Man, this is where everything happened last night. I think someone spilled an entire drink on the couch. Someone's gonna kill me if they see it.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Yeah, I don't really come down here. It's creepy as hell. Also, why does this house even have so many locked doors?",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "dude, I was literally just trying to find my phone. Don't make it weird.",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "Okay, this is officially getting out of hand. I mean, {victim} was literally here yesterday. This whole situation is messed up.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "I don't wanna accuse anyone, but {suspect} has been acting really weird. Then again, they can be weird. Don't tell them I said that.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "Wait, I remember something! Someone was arguing near the basement before everything happened. I couldn't hear what they were saying, though. Actually... I think I saw something on the floor down there. The person responsible may be {killer_clue}.",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "Look, I'm not gonna lie. I've been eating everything in sight because I'm stressed. If anyone asks, I haven't seen anything suspicious in here",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember talking to {victim} around here. They seemed pretty normal. Well, as normal as anyone can be at a party like that.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Okay, seriously, why is everyone suddenly interested in this basement? I swear I heard something down here last night.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "Can we just get out of here already? I haven't slept properly and I'm starting to lose my mind.",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "Three days. Three freaking days of this nightmare. I just want to go home. {victim} didn't deserve this, man.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I've been thinking about it, and I honestly think we should look at the people who keep changing their stories. Someone here is definitely lying.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "Okay, I found something earlier. I wasn't sure if it mattered, but here. Maybe you'll figure something out with it.",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "I can't even look at this kitchen anymore. Every time I come in here, I remember how normal everything used to be.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "This was supposed to be the best party of the year. Now look at us. Great job, me. Absolutely fantastic.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Listen, I don't know what's going on down here, but I'm done pretending everything is fine. Someone needs to explain what happened.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think I know more than I've been saying. I just didn't want to believe it was someone I knew.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    },
    {
        "name": "Lamarr",
        "role": "DJ",
        "type": "nervous",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Man... this is messed up. I was just here playing music. I didn't think the night would end like this.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "I don't know. Everyone was drinking and acting stupid. But I wouldn't be surprised if someone had a reason to be angry with somebody.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "Someone dropped this key? Aint sure what it’s good for but you can have it.",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Just getting some water. Been talking to people all night. My throat's killing me.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "Yeah, this is where I had my DJ setup. People were dancing like crazy. Honestly, the music was carrying the whole party.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Not much to say about this place. I came down here once to get some equipment. Didn't stay long.",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "Looking for my headphones. I swear someone keeps moving my stuff.",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "If {victim} was someone I cared about, this is personal. Even if we weren't close, nobody deserves to have their life end like this.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "I've noticed people aren't being honest. {suspect} especially. They're acting like everything is a joke, but I know them well enough to tell when something's wrong.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "I heard some shuffling downstairs in the basement. Aint sure though.",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "People keep coming in here looking for food. It's weird how everyone acts normal for a few seconds, then remembers what's happening.",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I was near the speakers most of the night. I remember hearing someone arguing, but the music was too loud to understand.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I came down here earlier. There's something out of place near the storage shelves. Didn't touch it.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I heard {quiet bookworm} used to spend more time around the library than at parties. I guess they weren't exactly made for this kind of chaos.",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I'm done pretending this is some kind of misunderstanding. Someone here knows exactly what happened. And I'm going to find out who.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I've been watching everyone. The person who did this isn't necessarily the loudest or the weirdest. It could be someone nobody would ever suspect.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "haven’t found anything yet dog my bad”",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "Not much has changed in here. Same food, same mess. Different atmosphere.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I've been thinking about that night. There was someone standing near the speakers who wasn't supposed to be there. I should've paid more attention.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "There's definitely something wrong with this room. I found evidence that someone was here after the party ended.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I haven't really been sleeping. Too much on my mind. I keep thinking about what could've happened if someone had noticed something earlier.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    },
    {
        "name": "Naomi",
        "role": "Sam's Best Friend",
        "type": "defiant",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Excuse me? Someone died? Are you actually serious? I leave {party host} alone for ONE night and suddenly we're in a crime documentary.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "Honestly? {suspect}. They give me weird vibes. They look like they would have a secret underground computer room or something.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "Is google fucking written on my forehead?? Don’t ask me.”",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Don't touch my drink. Seriously. I've already had enough people touching my stuff tonight.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "This is where {party host} embarrassed themself trying to dance. I have a video, but unfortunately I think my phone died.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Why would anyone willingly go down here? It smells like old socks and bad decisions.",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I was looking for my charger. Apparently, nobody in this house understands the concept of returning things.",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "Okay, this is actually horrible. I know we all joke around, but this isn't funny anymore. I just want to leave.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "I don't trust {suspect}. They've been following people around asking questions. Like, bro, you're not Sherlock Holmes.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "I overheard someone talking about the basement. They said something about a key being missing. Maybe you should look around the living room.",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "The snacks keep disappearing from this kitchen. I swear, if it happens one more time...",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember {victim} standing near the window. They looked upset about something. I didn't think much of it at the time.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I heard someone down here last night. I didn't investigate because, unlike some people, I actually have survival instincts.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "{suspect} was looking for something earlier. I don't know what, but they seemed pretty nervous. Maybe ask them.",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I swear, if the person who did this is standing right in front of me, I might actually lose it. This whole thing is disgusting.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I'm starting to think it's someone who has been acting way too normal. Everyone is freaking out except for one or two people. That's suspicious.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "Fine. I found this earlier. I was going to keep it, but I guess you need it more than I do.",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "I haven't eaten properly in two days. This house is officially cursed. Even the fridge is depressing.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "Everyone keeps pretending they're fine, but it isn't convincing. I know my best friend better than anyone here.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I swear someone has been moving things around down here. The storage boxes weren't like that yesterday.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "Honestly, I just want to sleep. But every time I close my eyes, I remember that we're trapped here with a murderer.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    },
    {
        "name": "Lorelei",
        "role": "Quiet Bookworm",
        "type": "quiet",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Oh... this is awful. I really hope everyone is okay. I don't think any of us expected something like this to happen.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "I don't want to accuse anyone. Maybe it was just an accident? I know that sounds stupid, but I don't want to believe someone here could do something like that.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "I found this key on the floor earlier, it might help!”",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Oh, hi! I was just getting some water. I'm not really used to being around so many people.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "{dj} played some really good music last night. I actually enjoyed myself more than I thought I would.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I don't really like it down here. It's dark and a little scary. I only came down because I thought I heard something.",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think someone left a book here. It's probably not important, but I recognize the cover.",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I can't stop thinking about {victim}. It's strange how quickly everything can change. Yesterday we were all laughing together.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "I noticed {suspect} was acting strange yesterday. But they can be a little awkward, so maybe I'm just overthinking it.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "I think I heard some footsetps when iwas trying to sleep? Not to sure though.”",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "I was here earlier making tea. I heard two people talking outside the kitchen, but I couldn't recognize their voices.",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember {dj} being here for most of the party. They were busy with the music, so I don't think they noticed everything happening around them.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I heard footsteps coming from downstairs last night. They sounded like someone was in a hurry.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think this room belonged to someone who left something important behind. There's a drawer that doesn't seem to close properly.",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I just wish we could go back to before all of this happened. Everything feels different now. I don't think I'll ever forget this.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I think the person responsible is someone who had a reason to hide something. Maybe we should stop looking at who seems suspicious and start looking at who has the most to lose.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "I haven’t found much. Sorry……",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "I haven't really been hungry. I keep forgetting to eat. It's strange how something so ordinary can feel so difficult right now.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember hearing someone arguing here. I didn't want to get involved, but I wish I had listened more carefully.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I found something that definitely wasn't here before. I think someone has been trying to hide it.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think I've figured something out. I'm just scared that if I tell the wrong person, things could get worse.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    },
    {
        "name": "Jayson",
        "role": "Basketball Player",
        "type": "arrogant",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Wait, someone died? Like... actually died? Dude, that's insane. I thought we were just gonna have a normal weekend.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "I don't know, man. Everyone seems pretty chill. Maybe {suspect}? They were standing around looking suspicious. But honestly, I don't know.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "I found something near the stairs. Looked like a key or something. I don't know what it opens, but you can have it.",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Yo! You hungry? I'm starving. I swear I've been eating every thirty minutes.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "This is where we were playing music and dancing. I think I accidentally broke something here. Don't tell {party host}.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "Bro, this place is huge. I was looking for some weights earlier, but I couldn't find anything.",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think I left my basketball shoes in here. Wait, why are you looking at me like that?",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "Man, this is getting really serious. I don't even know what to say. I just hope we figure out who did it.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "I think we should be careful about {suspect}. They seem nervous whenever someone mentions the murder. But maybe they're just scared. I don't want to blame anyone without knowing.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "Wait, I remember something! I saw someone near the bedroom holding something shiny. Could've been a key, maybe. I wasn't really paying attention.",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "Have you seen the cereal? I swear someone ate the entire box. This is honestly worse than the murder situation. Okay, not worse, but still.",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I was here talking to one of the guests yesterday. They seemed worried about something. I wanted to ask, but I didn't want to make things awkward.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I heard something fall down here earlier. Probably nothing, but there's a box that's been moved.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I was looking for my hoodie. I think I left it here after the party. Wait... why is there a drawer open?",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "This is honestly the worst week ever. I just want everyone to be okay. I don't care about anything else.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I think we should look at the evidence. Not just accuse people because they're weird. I mean, if being weird was illegal, half of us would be in prison.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "sorry bro haven’t seen much”",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "Okay, I officially hate this kitchen. There's no food left and everyone keeps acting like we're in some detective movie.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember something from the first night. Someone was standing near the door when everyone else was dancing. I thought they were just tired.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I found a weird mark near the storage area. Looks like someone dragged something across the floor.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "Look, I know I'm not the smartest guy here, but something doesn't add up. Someone is definitely lying.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    },
    {
        "name": "Daniel",
        "role": "Awkward Nerd",
        "type": "secretive",
        "dialogues": [
            {
                "topic": "murder",
                "response": "Wait, what? Someone died? Oh my God. I literally thought this was just going to be a normal party. Well, as normal as the host's parties can be.",
                "required_night": 1
            },
            {
                "topic": "suspect",
                "response": "I mean... statistically speaking, one of the people here must have done it. Sorry. That sounded less weird in my head.",
                "required_night": 1
            },
            {
                "topic": "hint",
                "response": "I noticed something strange near the bookshelf. I didn't touch it because, you know, fingerprints and stuff. I watch a lot of crime documentaries.",
                "required_night": 1
            },
            {
                "topic": "kitchen",
                "response": "Oh, hi. I was just looking for some water. I don't really know what to say to people right now.",
                "required_night": 1,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "This is where {party host} was standing most of the night. They were talking to everyone. I remember because I was... also in the room. Obviously.",
                "required_night": 1,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I actually looked around down here earlier. There are some old storage boxes and a locked door. Kind of interesting, honestly.",
                "required_night": 1,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I think someone left their phone charger here. Not mine, obviously. I mean, maybe mine. I have the same one.",
                "required_night": 1,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I don't really know how to process this. I keep replaying everything from last night in my head. Maybe I missed something important.",
                "required_night": 2
            },
            {
                "topic": "suspect",
                "response": "{suspect} has been acting strangely. But I don't think they would do something like this. I mean, I know them... well, sort of. We're not exactly close.",
                "required_night": 2
            },
            {
                "topic": "hint",
                "response": "sorry man I haven’t really found anything.”",
                "required_night": 2
            },
            {
                "topic": "kitchen",
                "response": "I came here earlier because I couldn't sleep. I think someone had been looking through the cabinets. There was something missing.",
                "required_night": 2,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember hearing someone mention the basement. They sounded upset. I couldn't see who it was because the lights were off.",
                "required_night": 2,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I found a locked storage box. I think it belongs to someone who was at the party. There might be something useful inside.",
                "required_night": 2,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I noticed that one of the drawers had been opened. I don't think anyone has mentioned it yet, but it could be important.",
                "required_night": 2,
                "required_location": "Bedroom"
            },
            {
                "topic": "murder",
                "response": "I've been trying to stay calm, but I'm honestly terrified. I keep thinking that whoever did this has been standing right next to us the entire time.",
                "required_night": 3
            },
            {
                "topic": "suspect",
                "response": "I think we should pay attention to contradictions. Someone told me they were in one room, but another person remembers seeing them somewhere else. That can't just be a coincidence.",
                "required_night": 3
            },
            {
                "topic": "hint",
                "response": "Okay, I've been keeping this to myself, but I found something that might connect two of the people here. I think you should take a look. It also fits this detail: {killer_detail}.",
                "required_night": 3
            },
            {
                "topic": "kitchen",
                "response": "I haven't really eaten anything. Every time I walk into a room, someone starts asking me questions. I'm beginning to feel like I'm the main suspect.",
                "required_night": 3,
                "required_location": "Kitchen"
            },
            {
                "topic": "living room",
                "response": "I remember {party host} laughing here on the first night. It feels strange thinking about that now. Everything was so normal.",
                "required_night": 3,
                "required_location": "Living Room"
            },
            {
                "topic": "basement",
                "response": "I think someone has been using this room to hide things. There are footprints near the storage shelves. I don't think they belong to someone who spends much time down here.",
                "required_night": 3,
                "required_location": "Basement"
            },
            {
                "topic": "bedroom",
                "response": "I found something behind the bed earlier. I don't know who put it there, but I think it could be important.",
                "required_night": 3,
                "required_location": "Bedroom"
            }
        ]
    }
]
