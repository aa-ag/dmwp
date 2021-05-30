from collections import Counter


def calculate_mode(l):
    count = Counter(l)
    frequencies = count.most_common()
    most_repeated_number = frequencies[0][1]

    modes = list()

    for number in frequencies:
        if number[1] == most_repeated_number:
            modes.append(number[0])
    return modes


if __name__ == '__main__':
    m = calculate_mode([5, 5, 5, 4, 4, 4, 9, 1, 3])
    print("The mode(s) in the list are:")
    for i in m:
        print(i)
