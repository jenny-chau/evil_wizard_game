from abc import abstractmethod
import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, heal_amount=10, mana_recovery_rate=5, mana=100):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
        # temp_attack_power is set to 0 when opponent evades attack. It gets reset to None after the turn.
        self.temp_attack_power = None
        
        self.max_health = health
        self.heal_amount = heal_amount
        
        self.mana = mana
        self.max_mana = mana
        self.mana_recovery_rate = mana_recovery_rate

    # current_attack parameter can be passed in to manually set the attack power (such as for 2x or 3x damage)
    def attack(self, opponent, current_attack = 0):
        original_opponent_health = opponent.health
        
        # Check if evade special ability was used by opponent
        if self.temp_attack_power == 0:
            print(f" -> {self.name} attempts to attack, but {opponent.name} evades the attack!")
            self.temp_attack_power = None
            return

        # Check if attack misses (5% chance of missing)
        does_attack_miss = random.randint(1,100) <= 5
        
        if does_attack_miss == True:
            print(f" -> {self.name} attack missed!")
            return
        
        # Randomize attack to +/- 5 attack power
        if current_attack == 0:
            current_attack = random.randint(self.attack_power-5, self.attack_power+5)

        # Attack opponent
        opponent.health -= current_attack
        
        # Update opponent health to 0 if value is negative
        if opponent.health < 0:
            opponent.health = 0
        
        print(f" -> {self.name} attacks {opponent.name} for {current_attack} damage! {opponent.name}'s health went from {original_opponent_health} to {opponent.health}.")
            
    @abstractmethod 
    def special_ability(self, opponent):
        print("Should be overridden by subclasses")
    
    # Heal character
    def heal(self):
        # If health is almost to max, heal to max
        if self.health + self.heal_amount > self.max_health:
            heal_amount = self.max_health - self.health
            self.health = self.max_health
            
        # Else heal the standard amount
        else:
            heal_amount = self.heal_amount
            self.health += self.heal_amount
            
        print(f" -> {self.name} healed {heal_amount} points! Health = {self.health}")

    # Used to check if character has enough mana to perform special ability
    def has_enough_mana(self,amount):
        if self.mana >= amount:
            return True
        else:
            return False

    # Recovery mana method
    def mana_recovery(self):
        if self.mana < self.max_mana - self.mana_recovery_rate:
            self.mana += self.mana_recovery_rate
            print(f" -> {self.name}'s Mana replenished by {self.mana_recovery_rate}. Mana = {self.mana}")
        elif self.mana != self.max_mana:
            self.mana = self.max_mana
            print(f" -> {self.name}'s Mana replenished to max. Mana = {self.mana}")
    
    # Display character stats (health, attack power, and mana)
    def display_stats(self):
        print(f" -> {self.name}'s Stats - Health: {self.health}/{self.max_health}, Average Attack Power: {self.attack_power}, Mana: {self.mana}")
        
    # Displays the special abilities along with the mana cost / whether character has enough Mana for that ability. Returns a list of abilities the character has enough mana for.
    def get_display_special_abilities(self, special_abilities):
        ability_choices=[]
        
        print(f"\nSpecial Abilities: (Available Mana = {self.mana})")
        
        for key, value in special_abilities.items():
            if self.has_enough_mana(value.get('mana_cost')): 
                print(f"{key}. {value.get('ability_name')} Cost {value.get('mana_cost')} Mana")
                ability_choices.append(key)
            else:
                print(f"{key}. {value.get('ability_name')} !! NOT ENOUGH MANA !!")
            
        print("3. Back")
        
        return ability_choices