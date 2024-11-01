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

def delete_skill():
    category = input("Enter the category you want to delete: ")
    if category in character_skills:
        del character_skills[category]
        print(f"Category '{category}' has been deleted.")
    else:
        print("Category not found!")

def display_skills():
    print(character_skills)

while True:
    ask = input('Continue? (+/-): ')
    if ask == '+':
        while True:
            action = input("Do you want to Add Skill (1), Level Up Skill (2), or Delete Category (3)? ")
            if action in ['1', '2', '3']:
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
        elif action == '3':
            delete_skill()
        display_skills()
    else:
        break
