from collections import Counter

simple_list = [1, 2, 3, 4, 5, 2]
c = Counter(simple_list)
print(c.most_common())
