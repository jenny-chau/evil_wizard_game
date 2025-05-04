from evil_wizard_game import main
import random
import builtins
import sys
from io import StringIO

class AutoInput:
    def __init__(self):
        # Potenial action choices when playing the game
        self.inputs = ["1", "2", "3", '4']
    
    def __call__(self, prompt=""):
        # Whenever the game requires an input, this function will be called and a random choice from the list of inputs will be returned
        return random.choice(self.inputs)

def test_game(num_runs=10):
    # Clear the log file
    with open("game_test_log.txt", "w") as log_file:
        log_file.write("")
    
    for i in range(num_runs):
        print(f"\n ---------- Running game {i + 1} --------- ")
        
        # Reassign built-in input with the automated input
        auto_input = AutoInput()
        builtins.input = auto_input
        
        try:
            # Create a StringIO object to store print statements from the game in memory
            new_out = StringIO()

            # Redirect the print outputs (normally printed to the terminal) to the StringIO object to be accessed by the code later
            sys.stdout = new_out
            # Play the game
            main()
            
            # Store the game output from the new_out StringIO object
            output = new_out.getvalue()
              
            # Restore the program to print to the terminal
            sys.stdout = sys.__stdout__
            
            # Log the output to the .txt file
            with open("game_test_log.txt","a") as log_file:
                log_file.write(f"\n ---------- Running game {i + 1} --------- ")
                log_file.write(output)
                
            # To easily visualize if the game was completed or if there was an error, print the game result in the terminal
            if "Congratulations!" in output:
                print("Victory")
            elif "Better luck next time!" in output:
                print("Defeat")
            else:
                print("Error: Unknown outcome")
                
        except Exception as e:
            # Restore print to the terminal
            sys.stdout = sys.__stdout__
            print(f"Error during game {i+1}: {e}")
            
            # Log error into .txt file
            with open("game_test_log.txt", "a") as log_file:
                log_file.write(f"Game {i + 1} has an error and stopped running.")
    
            print(f"Game {i + 1} has an error and stopped running.")
            
if __name__ == "__main__":
    # test the game as many times as needed
    test_game(1) 
