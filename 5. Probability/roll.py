############------------ IMPORT(S) ------------############
import matplotlib.pyplot as plt
import random


############------------ FUNCTION(S) ------------############
def roll():
    '''
     Roll a die until the total score is N
    '''
    return random.randint(1, 6)


############------------ TEST CASES ------------############
target_score = 20

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    score = 0
    rolls = 0
    while score < target_score:
        roll_the_die = roll()
        rolls += 1
        print(f"rolled {roll_the_die}")
        score += roll_the_die

    print(f"score of {score} reached after {rolls} rolls")
