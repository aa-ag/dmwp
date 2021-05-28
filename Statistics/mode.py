from collections import Counter

simple_list = [1, 2, 3, 4, 5, 2]
mode = Counter(simple_list)
print(mode.most_common(1)[0][0])
