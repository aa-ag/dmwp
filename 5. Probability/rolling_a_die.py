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
    print(f"The probability of rolling a prime: {probability_calculation}")