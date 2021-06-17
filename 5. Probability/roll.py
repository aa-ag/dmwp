'''
Roll a die until the total score is N
'''

import matplotlib.pyplot as plt
import random


target_score = 20

def roll():
    return random.randint(1, 6)

if __name__ == "__main__":
    score = 0
    rolls = 0
    while score < target_score:
        roll_the_die = roll()
        rolls += 1
        print(f"rolled {roll_the_die}")
        score += roll_the_die

    print(f"score of {score} reached after {rolls} rolls")

'''
 rolled 2
rolled 3
rolled 1
rolled 2
rolled 1
rolled 1
rolled 2
rolled 4
rolled 5
score of 21 reached after 9 rolls
'''