def is_factor(a, b):
    '''
     when a non-zero integer "a" divides
     another integer "b", leaving a remainder 
     of zero, "a" is said to be a factor of "b"
    '''
    if b % a == 0:
        return True
    return False


print(is_factor(4, 1024))  # True
print(is_factor(4, 1023))  # False
