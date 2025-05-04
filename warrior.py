from character import Character

# Warrior class (inherits from Character)
class Warrior(Character):
    special_abilities = {
        '1': {
            'ability_name': "Gym Rat (attack buff +20%)",
            'mana_cost': 20
        },
        '2': {
            'ability_name': "Enraged (double attack)",
            'mana_cost': 30
        }
    }
    
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        # Used to check which abilities can be executed based on the amount of mana available
        ability_choices = []
        
        # Display special abilities and adds the special abilities that can be played (enough mana) to the ability_choices list
        ability_choices.extend(self.get_display_special_abilities(self.special_abilities))
        
        while True:
            ability = input("\nSelect a special ability: #").strip()
            
            if ability == "1" and ability in ability_choices:
                self.mana -= self.special_abilities['1']['mana_cost']
                self.attack_power = round(self.attack_power * 1.2)
                print(f" -> After an extensive gym session, {self.name} is now extra buff, increasing the average attack power to {self.attack_power}!")
                return
            elif ability == "2" and ability in ability_choices:
                current_attack = self.attack_power * 2
                print(f" -> Blinded by rage, {self.name} inflicts double damage!")
                self.attack(opponent,current_attack)
                self.mana -= self.special_abilities['2']['mana_cost']
                return
            elif ability == "3":
                return "Back"
            else:
                print(" -> Not enough mana or invalid input. Please try again.")
