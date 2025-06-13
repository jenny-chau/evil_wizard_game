def welcome():
    print("""\n---- Welcome to the Evil Wizard Game! ----\n
This is how the game works:
* First, You will choose a character class to play as (Warrior, Mage, Archer, or Paladin).
* Each character has their own attack power and health. They also each have their own special abilities that use mana (such as buffs, double damage, evade). Buffs are permanent.
* You will battle against the evil wizard who also has mana and special abilities.
* Mana replenishes a small amount at the start of each round, so use it wisely!
* Normal attacks range +/-5 the attack power, with a 5% change of missing.

Each round:
Player's turn:
    Choose an action (attack, special ability, heal 10 health). You may also view your stats at this time.
Enemy's turn:
    Heals 5 health until max, attacks or uses a special ability.

Game end:
Either the player or the wizard reaches a health of 0 and is defeated.

Best of luck!\n
          """)