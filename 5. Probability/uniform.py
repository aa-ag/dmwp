############------------ IMPORT(S) ------------############
import random

############------------ FUNCTION(S) ------------############
def toss():
    '''
     simulate a toss where
     heads is twice as likely as
     tails (coin)
    '''
    if random.random() < 2/3:
        return "heads"
    return "tails"

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(toss())