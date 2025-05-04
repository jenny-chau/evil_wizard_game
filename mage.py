from character import Character

# Mage class (inherits from Character)
class Mage(Character):
    special_abilities = {
        '1': {
            'ability_name': "Hypnosis (enemy damage -15%)",
            'mana_cost': 20
        },
        '2': {
            'ability_name': "Self-Duplicate (evades next attack)",
            'mana_cost': 30
        }
    }
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        ability_choices = []
        
        ability_choices.extend(self.get_display_special_abilities(self.special_abilities))

        while True:
            ability = input("\nSelect a special ability: #").strip()

            if ability == "1" and ability in ability_choices:
                opponent.attack_power = round(opponent.attack_power * 0.85)
                self.mana -= self.special_abilities['1']['mana_cost']
                print(f" -> {opponent.name} is hyptonized and its attack fell 15% to {opponent.attack_power}.")
                break
            elif ability == "2" and ability in ability_choices:
                opponent.temp_attack_power = 0
                self.mana -= self.special_abilities['2']['mana_cost']
                print(f" -> Many copies of {self.name} are running around now, making {opponent.name} confused!")
                break
            elif ability == "3":
                return "Back"
            else:
                print(" -> Not enough mana or invalid input. Please try again.")
