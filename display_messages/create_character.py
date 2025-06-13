from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin
from display_messages.welcome import welcome

# Function to create a character of the user's choosing
def create_character():
    welcome()
    name = input("Enter your character's name: ")
    
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    print("5. Show character special abilities")
    
    while True:
        class_choice = input("\nEnter the number of your class choice: ")
        
        if class_choice == '1':
            print("You are now a Warrior!!\n\n<----Commence battle against the Evil Wizard---->\n")
            return Warrior(name)
        elif class_choice == '2':
            print("You are now a Mage!!\n\n<----Commence battle against the Evil Wizard---->\n")
            return Mage(name)
        elif class_choice == '3':
            print("You are now an Archer!!\n\n<----Commence battle against the Evil Wizard---->\n")
            return Archer(name)
        elif class_choice == '4':
            print("You are now a Paladin!!\n\n<----Commence battle against the Evil Wizard---->\n")
            return Paladin(name)
        elif class_choice == '5':
            print("\nSpecial Abilities List:")
            characters = [Warrior, Mage, Archer, Paladin]
            for character in characters:
                print(f"{character.__name__}:")
                for key, value in character.special_abilities.items():
                    print(f"    {key}. {value.get('ability_name')} -> Cost {value.get('mana_cost')} Mana")

        else:
            print("ERROR: Invalid option. Please try again.")