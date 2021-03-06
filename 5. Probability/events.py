# fin the probability of either
# event A or event B taking place

space = {1, 2, 3, 4, 5, 6}

# is prime
event_a = {2, 3, 5}

# is odd
event_b = {1, 3, 5}

# event
e = event_a.union(event_b)

probability = len(e)/len(space)

clean_result = lambda x: x - x % 0.01

print(clean_result(probability))