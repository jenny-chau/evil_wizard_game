from character import Character

# Paladin class (inherits from Character)
class Paladin(Character):
    special_abilities = {
        '1': {
            'ability_name': "Holy Strike (attack buff +20%)",
            'mana_cost': 20
        },
        '2': {
            'ability_name': "Divine Mana (mana recovery rate +5 mana/round)",
            'mana_cost': 15
        }
    }
    
    def __init__(self,name):
        super().__init__(name, health=130, attack_power=30)
        
    def special_ability(self, opponent):
        ability_choices = []
        
        ability_choices.extend(self.get_display_special_abilities(self.special_abilities))

        while True:
            ability = input("\nSelect a special ability: #").strip()

            if ability == "1" and ability in ability_choices:
                self.attack_power = round(self.attack_power * 1.2)
                self.mana -= self.special_abilities['1']['mana_cost']
                print(f" -> Buff activated! Average attack power is now {self.attack_power}.")
                break
            elif ability == "2" and ability in ability_choices:
                self.mana_recovery_rate += 5
                self.mana -= self.special_abilities['2']['mana_cost']
                print(f" -> {self.name} found a bottle of cloudy, thick blue-green liquid in the corner and decided to take a sip. Feeling extra energized, {self.name}'s Mana recovery rate is now {self.mana_recovery_rate}.")
                break
            elif ability == "3":
                return "Back"
            else:
                print(" -> Not enough mana or invalid input. Please try again.")
