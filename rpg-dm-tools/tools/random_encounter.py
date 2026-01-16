import random


def random_encounter(biome: str, difficulty: str|None=None, party_level: int|None=None, party_size: int|None=None, seed: int|None=None) -> dict:
    encounters = {
        'forest': [
            {'encounter_name': 'Elven Gathering', 'hook': 'You see a group of elves celebrating.', 'scene': 'A serene glade filled with laughter.', 'combatants': [], 'twist': 'They invite you to join.', 'noncombat_out': 'You gain new allies.', 'loot': []},
            {'encounter_name': 'Dire Wolf Pack', 'hook': 'A howl echoes through the trees.', 'scene': 'Shadowy figures lurk among the shadows.', 'combatants': ['Dire Wolf'], 'twist': 'They are protecting their den.', 'noncombat_out': 'You sneak by unnoticed.', 'loot': []},
            {'encounter_name': 'Mysterious Stranger', 'hook': 'A hooded figure appears.', 'scene': 'The forest grows quiet around you.', 'combatants': [], 'twist': 'The figure provides valuable information.', 'noncombat_out': 'You learn local lore.', 'loot': ['Ancient Map']},
            {'encounter_name': 'Bridge Troll', 'hook': 'A grumpy troll blocks the path.', 'scene': 'A rickety old bridge with a fierce guardian.', 'combatants': ['Troll'], 'twist': 'He offers a riddle instead of a fight.', 'noncombat_out': 'Solving the riddle earns you safe passage.', 'loot': ['Gold Coin']},
            {'encounter_name': 'Giant Spider', 'hook': 'Silk threads block the path.', 'scene': 'An eerie silence falls around you.', 'combatants': ['Giant Spider'], 'twist': 'It is guarding its lair.', 'noncombat_out': 'You find a way to avoid it.', 'loot': ['Webbed Treasure']}
        ],
        'city': [
            {'encounter_name': 'Market Thief', 'hook': 'A thief tries to grab your pouch.', 'scene': 'Bustling market filled with vendors.', 'combatants': ['Thief'], 'twist': 'He is surprisingly nimble.', 'noncombat_out': 'You retrieve your money successfully.', 'loot': []},
            {'encounter_name': 'City Guard', 'hook': 'You are approached by a guard.', 'scene': 'The streets are patrolled by vigilant guards.', 'combatants': ['Guard'], 'twist': 'He seeks your help.', 'noncombat_out': 'You gain a new quest.', 'loot': []},
            {'encounter_name': 'Street Performer', 'hook': 'A juggler captures the crowd’s attention.', 'scene': 'Lively street filled with cheer.', 'combatants': [], 'twist': 'He has insider info about a quest.', 'noncombat_out': 'You learn about hidden places.', 'loot': ['Trinket']},
            {'encounter_name': 'Underground Fight Club', 'hook': 'You hear shouts and cheers.', 'scene': 'An underground arena filled with excitement.', 'combatants': ['Fighter'], 'twist': 'You are challenged to duel.', 'noncombat_out': 'Winning earns you prestige.', 'loot': ['Prize Money']},
            {'encounter_name': 'Noble’s Request', 'hook': 'A noble approaches you.', 'scene': 'The opulence of high society contrasts with the streets.', 'combatants': [], 'twist': 'He needs a discreet favor.', 'noncombat_out': 'You gain influence.', 'loot': ['Gold Bar']}
        ],
        'dungeon': [
            {'encounter_name': 'Ancient Guardian', 'hook': 'A statue comes to life.', 'scene': 'A dark room illuminated by eerie light.', 'combatants': ['Guardian'], 'twist': 'It will not attack if you answer correctly.', 'noncombat_out': 'Answering the riddle allows passage.', 'loot': ['Ancient Artifact']},
            {'encounter_name': 'Zombie Horde', 'hook': 'You hear groans echoing off the walls.', 'scene': 'Rotting corpses surround you.', 'combatants': ['Zombie'], 'twist': 'They are slow but many.', 'noncombat_out': 'You easily evade them.', 'loot': ['Old Armor']},
            {'encounter_name': 'Treasure Chest', 'hook': 'A chest sits in the middle of the room.', 'scene': 'A glimmer catches your eye.', 'combatants': [], 'twist': 'It is trapped!', 'noncombat_out': 'Spotting the trap allows you to open it safely.', 'loot': ['Gold Coins', 'Potion']},
            {'encounter_name': 'Cult Ritual', 'hook': 'You stumble upon a dark ritual.', 'scene': 'An altar surrounded by chanting cultists.', 'combatants': ['Cultist'], 'twist': 'They will not notice you if you stay quiet.', 'noncombat_out': 'Leaving quietly earns you safe passage.', 'loot': []},
            {'encounter_name': 'Guardian Beast', 'hook': 'A large beast prowls.', 'scene': 'Muffled growls echo through the stone chamber.', 'combatants': ['Beast'], 'twist': 'It’s protecting something valuable.', 'noncombat_out': 'You sneak past it successfully.', 'loot': ['Rare Gem']}
        ]
    }

    if seed is not None:
        rng = random.Random(seed)
    else:
        rng = random

    if biome not in encounters:
        raise ValueError('Invalid biome selected.')

    weighted_encounters = []
    for encounter in encounters[biome]:
        weight = 1  # Default weight
        if difficulty == 'easy':
            weight *= 3 if not encounter['combatants'] else 1
        elif difficulty == 'hard':
            weight *= 1 if not encounter['combatants'] else 2
        weighted_encounters.extend([encounter] * weight)

    selected_encounter = rng.choice(weighted_encounters)
    return {**selected_encounter, 'biome': biome, 'difficulty': difficulty, 'party_level': party_level, 'party_size': party_size}
