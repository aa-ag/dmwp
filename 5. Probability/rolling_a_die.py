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
    pass