"""
Goal : Build a guess the state capital game.
    
Step 1) Read the text file. Try and understand what each line shows here.
Step 1-a) Determine a data structure from what we have learnt that will be well suited
     to store state - capital pairs for the game. Create a GLOBAL variable for this
     data structure
Step 1-b) Similar to what I did in Hangman, create a function that opens the text file
     based on file path. For each line in text file, create the pair.
     Populate the global variable you created with all contents of the text file.
     Print the variable to see if its contents are printed as you desire.
     eg. State: Capital, Another_State: Capital... (is how we would want to see each pair)

Step 2) Create a main function.
Step 2a) Create a variable to randomly generate a state from the data structure you
     created in Step 1-a. Use random.choice() to get this state.
Step 2b) Now ask user to guess the capital of this STATE
Step 2c) Try and handle input cases like empty string as answer (Repeat question)

Step 3) Create a function that compares the player's answer with the right answer for
     the state. If the answer is right, print appropriate message, else, print you're
     wrong and then provide the right answer
Hint : The dictionary uses a key-value pair. e.g get("ALABAMA") will return Montgomary

Additional:
    1) You can create a function for play again like we did in Hangman.
    2) You can also add a counter for score.
    3) If you really want to build it into a full-fledged quiz show kind of game that
    would look good in your list of projects, add levels. 
    For each level, determine no. of questions to be asked and use the score counter.
"""

import random
# STATE_CAPITAL = Assign empty data structure of appropriate type here
STATE = ""
CAPITAL = ""

def func_name(path):
    """
    param: path
    return: STATE_CAPITAL
    """
    
# ANOTHER FUNCTION TO CHECK ANSWER GOES HERE

def main():
    global STATE, CAPITAL
    """
    1. Call a function that reads contents of the text file
    2. Randomly choose state here
    3. Get user input for a question that asks player to guess capital of the
    randomly chosen state
    4. Create another variable that stores capital of this state
    5. Call a function that compares player answer with actual CAPITAL and prints
    appropriate message
    """
    path = "file path goes here"
    
if __name__ == '__main__':
    main()
