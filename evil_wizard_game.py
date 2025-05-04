import random
from evil_wizard import EvilWizard
from create_character import create_character
from display_player_action_menu import display_player_action_menu

# Battle continues until one party is defeated (Health = 0)
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n------ Your Turn ------")
        
        # Mana recovery
        player.mana_recovery()
        
        display_player_action_menu()
        
        while True:
            choice = input("\nChoose an action (1-4): ")

            if choice == '1':
                player.attack(wizard)
                break
            elif choice == '2':
                result = player.special_ability(wizard)
                
                # If the player returns from the special abilities menu without selecting a special ability, the action menu will display again for the player to choose from
                if result != "Back":
                    break
                else: 
                    display_player_action_menu()
                    continue
            elif choice == '3':
                # Asks for confirmation about whether the player wants to heal for less than the max possible amount 
                if player.health > player.max_health - player.heal_amount:
                    verify = input(f"Are you sure you want to heal? You will heal {player.max_health - player.health} of {player.heal_amount} possible health points. (Y or N): ").upper()
                    if verify == "Y":
                        player.heal()
                        break
                    elif verify == "N":
                        print("Please choose another action.")
                    else:
                        print("ERROR: Invalid input. Please choose another action to take.")
                        
                    # Display the action menu for the player again
                    display_player_action_menu()
                    continue
                else:
                    player.heal()
                    break
            elif choice == '4':
                # Displaying player stats does not use an action so loop will continue
                player.display_stats()
            else:
                print("ERROR: Invalid choice. Try again.")

        # Evil Wizard turn
        if wizard.health > 0:
            print(f"\n------ {wizard.name} Turn ------")
            # Wizard mana recovery
            wizard.mana_recovery()
                
            # Wizard heal
            wizard.heal()
            
            # Wizard attack (#1 = normal attack, #2 = +50 health, #3 = triple attack, #4 = +30 mana)
            available_abilities = [1]
            
            # Update available_abilities based on avilable mana and health/mana levels
            if wizard.mana >= 40:
                available_abilities.extend([2, 3, 4])
                if wizard.health > 0.8 * wizard.max_health:
                    available_abilities.remove(2)
                if wizard.mana > 0.8 * wizard.max_mana:
                    available_abilities.remove(4)
            elif wizard.mana >= 35:
                available_abilities.append(3)
            
            # randomize the wizard's move
            move = random.choice(available_abilities)
            if move == 1:
                wizard.attack(player) 
            else:
                wizard.special_ability(player, move)

    print("\n<-------End Battle------->")
    if player.health <= 0:
        print(f"{player.name} has been defeated. Better luck next time!\n")
    elif wizard.health <= 0:
        print(f"Congratulations! {wizard.name} has been defeated by {player.name}!\n")
    else:
        print("error")

# Main function to play the game
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

# Ensures game initiates when script is run directly and not upon import as a module
if __name__ == "__main__":
    main()
