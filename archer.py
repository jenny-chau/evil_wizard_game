from character import Character

# Archer class (inherits from Character)
class Archer(Character):
    special_abilities = {
        '1': {
            'ability_name': "Quick Shot (double attack)",
            'mana_cost': 30
        },
        '2': {
            'ability_name': "Evade (evade next attack)",
            'mana_cost': 30
        }
    }
    
    def __init__(self,name):
        super().__init__(name, health=100, attack_power=20)
    
    def special_ability(self, opponent):
        # Used to check which abilities can be executed based on the amount of mana available
        ability_choices = []
        
        # Display special abilities and adds the special abilities that can be played (enough mana) to the ability_choices list        
        ability_choices.extend(self.get_display_special_abilities(self.special_abilities))

        while True:
            ability = input("\nSelect a special ability: #").strip()

            if ability == "1" and ability in ability_choices:
                current_attack = self.attack_power * 2
                print(f" -> With a sudden burst of energy, {self.name} inflicts double damage!")
                self.mana -= self.special_abilities['1']['mana_cost']
                self.attack(opponent,current_attack)
                break
            elif ability == "2" and ability in ability_choices:
                opponent.temp_attack_power = 0
                self.mana -= self.special_abilities['2']['mana_cost']
                print(f" -> {self.name} found a box to hide in!")
                break
            elif ability == "3":
                return "Back"
            else:
                print(" -> Not enough mana or invalid input. Please try again.")
