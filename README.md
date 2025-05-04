# Evil Wizard Game

## Project Overview
- In this game, you will choose between four different hero character classes (warrior, mage, archer, or paladin) and fight against The Dark Wizard. 
- This is a turn-based game played in the terminal.

## Main elements of the game
- Attack power, mana (for special abilities), and healing
    - On your (the hero's) turn, you will be able to choose between attack, special ability, or heal as your action. You will also recover a small amount of mana at the beginning of your turn.
    - On the evil wizard's turn, it will randomly choose between attack and special ability (significant heal, triple attack, or significant mana recovery). It also heals and recovers a small amount of mana at the start of its turn.
- Other Notes:
    - Each character type has its own special abilities. 
    - Normal attack ranges +/- 5 the character's attack power (attack damage to opponent is randomly chosen within that range)
    - There is a 5% chance of hero or enemy attack missing

## Languages used:
- Python (OOP, classes, objects)

## Code files
- Main game (evil_wizard_game.py)
     - Welcomes player and displays How to Play instructions (welcome.py)
     - Asks player for a character name and what class they want to play as (create_character.py)
        - Hero specific special abilities can be displayed at this time to help players decide on a character to play
     - Battle begins against The Dark Wizard
        - Action menu is displayed (display_player_action_menu.py) and waits for user input
- Character classes
    - Parent class: Character (character.py)
        - Contains methods for attack, heal, mana recovery, display stats, display special abilities
    - Child classes:
        - Initializes with subclass specific attributes, and contains their own method for using special abilities
        - Warrior (warrior.py)
        - Mage (mage.py)
        - Archer (archer.py)
        - Paladin (paladin.py)
        - EvilWizard (evil_wizard.py)
- Test files
    - test_game.py
        - Runs the game with randomized action choices
        - Can be run many times to look for potential bugs
        - Saves game logs in game_test_log.txt for review
            - Game logs in the .txt file are reset each time the test_game.py is run