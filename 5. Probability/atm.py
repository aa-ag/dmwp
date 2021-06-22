############------------ IMPORT(S) ------------############
import random
from collections import Counter as counter

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


def dispense():
    dollar_bills = [5, 10, 20, 50]
    
    probability_of_each = [1/6, 1/6, 1/3, 1/3]

    bill_index = get_index(probability_of_each)
    return dollar_bills[bill_index]

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    simulation = [dispense() for i in range(0, 101)]

    print(counter(simulation))
    # {50: 37, 20: 30, 5: 18, 10: 16}