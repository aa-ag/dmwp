############------------ IMPORT(S) ------------############
import random

############------------ FUNCTION(S) ------------############
def get_index(probability):
    '''
     simulate an ATM that dispenses 
     dollar bills of differente
     denominations
    '''
    c_probability = 0

    sum_probability = list()

    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)

    r = random.random()

    for index, sp in enumerate(sum_probability):
        if r <= sp:
            return index

    return len(probability) - 1

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass
