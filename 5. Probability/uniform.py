############------------ IMPORT(S) ------------############
import random
from collections import Counter as counter

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
    sample = list()
    for i in range(0, 1000001):
        sample.append(toss())

    c = counter(sample)
    # print(c)
    # Counter({'heads': 665675, 'tails': 334326})

    h = round((c['heads'] / len(sample)) * 100, 2)
    t = round((c['tails'] / len(sample)) * 100, 2)

    print(f"Heads: {h}% of the time -- Tails: {t}% of the time")
    # Heads: 66.69% of the time -- Tails: 33.31% of the time