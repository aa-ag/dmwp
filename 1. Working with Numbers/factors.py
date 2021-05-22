def is_factor(a, b):
    if b % a == 0:
        return True
    return False


print(is_factor(4, 1024))
