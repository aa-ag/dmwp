from collections import Counter


def calculate_mode(l):
    mode = Counter(l)
    return mode.most_common(1)[0][0]


if __name__ == '__main__':
    print(calculate_mode([1, 2, 3, 4, 5, 2, 8, 9, 2, 3, 4, 2, 8]))
