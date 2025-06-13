from characters.character import Character

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, heal_amount=5, mana_recovery_rate=15, mana=50)
        
    def special_ability(self, opponent, ability):
        # ability #2: heal 50 health up to max
        if ability == 2:
            # Check if adding 50 health will be greater than the max health
            if self.health >= self.max_health - 50:
                self.health = self.max_health
            else:
                self.health += 50
            self.mana -= 40
            print(f" -> {self.name} used a special ability, increasing its health significantly (+50 max increase up to its max health). Health = {self.health}.")
        
        # ability #3: triple attack
        elif ability == 3:
            print(f" -> {self.name} used a special ability and recruited some minions for a triple attack!")
            self.attack(opponent,self.attack_power * 3)
            self.mana -= 35
        
        # ability #4: mana recovery 30
        elif ability == 4:
            # Check if adding 30 mana will be greater than the max mana
            if self.mana >= self.max_mana - 30:
                self.mana = self.max_mana
            else:
                self.mana += 30
            self.mana -= 40
            print(f" -> {self.name} used a special ability, increasing its Mana significantly (+30 max increase up to its max Mana). Mana = {self.mana}.")
        
        # Error handling
        else:
            print(" -> Unknown ability. Defaulting to normal attack.")
            self.attack(opponent)