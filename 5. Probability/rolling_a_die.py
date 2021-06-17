def probability(space, event):
    return len(event) / len(space)

def check_prime(n):
    if n != 1:
        for factor in range(2, n):
            if n % factor == 0:
                return False
    else:
        return False
    return True


###--- DRIVER CODE ---###
if __name__ == "__main__":
    space = {i for i in range(1, 21)}
    primes = list()

    for i in space:
        if check_prime(i):
            primes.append(i)
    
    event = set(primes)
    probability_calculation = probability(space, event)

    print(f"Sample space: {space}")
    print(f"Event: {event}")
    print("The probability of rolling a prime: " + "%.2f" % probability_calculation)

'''
Sample space: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
Event: {2, 3, 5, 7, 11, 13, 17, 19}
The probability of rolling a prime: 0.40
'''