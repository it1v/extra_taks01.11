character_skills = {
    'Combat': {'Swords': 3, 'Bows': 2},
    'Magic': {'Fire': 1}
}

def add_skills(category, skill, level):
    if category in character_skills:
        character_skills[category][skill] = level
    else:
        character_skills[category] = {skill: level}

def level_up_skill():
    category = input("Enter the skill category: ")
    skill = input("Enter the skill you want to level up: ")
    
    if category in character_skills and skill in character_skills[category]:
        character_skills[category][skill] += 1
        print(f"{skill} in {category} has been leveled up to {character_skills[category][skill]}.")
    else:
        print("Skill not found!")

def display_skills():
    print(character_skills)

while True:
    ask = input('Continue? (+/-): ')
    if ask == '+':
        while True:
            action = input("Do you want to Add Skill or Level Up Skill? Print 1 or 2: ")
            if action in ['1', '2']:
                break
            else:
                print("Invalid input!")
        if action == '1':
            category = input("Category? ")
            skill = input("Skill? ")
            level = int(input("Level? "))
            add_skills(category, skill, level)
        elif action == '2':
            level_up_skill()
        display_skills()
    else:
        break