############------------ IMPORT(S) ------------############
import random
import collections

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
    dollar_bills = ['$5','$10', '$20', '$50']
    
    probability_of_each = [1/6, 1/6, 1/3, 1/3]

    bill_index = get_index(probability_of_each)
    return dollar_bills[bill_index]

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    simulation = [dispense() for i in range(0, 101)]

    count = collections.Counter(simulation)

    results = collections.OrderedDict(sorted(count.items()))
    
    for bill, prob in results.items():
        print(f"probability of getting a {bill} bill from this ATM: {prob}%")

    '''
    probability of getting a $10 bill from this ATM: 15%
    probability of getting a $20 bill from this ATM: 36%
    probability of getting a $5 bill from this ATM: 14%
    probability of getting a $50 bill from this ATM: 36%
    '''
    