def print_menu():
    print('Enter 1 to convert Kilometers to Miles')
    print('Enter 2 to convert Kilometers to Miles')


def kilometer_to_miles():
    kilometers = input('Enter number of kilometers:\n')
    return f"\n{int(kilometers) / 1.609} miles"


def miles_to_kilometers():
    miles = input('Enter number of miles:\n')
    return f"\n{int(miles) * 1.609} kilometers"


if __name__ == '__main__':
    print_menu()

    option = input('Which conversion would you like to do?\n')
    if option == '1':
        print(kilometer_to_miles())

    if option == '2':
        print(miles_to_kilometers())


# inches to meters
# (n * 2.54) / 100
# example:
# print((5 * 2.54) / 100)
# 0.127


# farenheit to celsius
# (F - 32) * (5/9)
# print((10 - 32) * (5/9))
# -12.222222222222223

# celsius to farenheit
# C * (9/5) + 32
# print(10 * (9/5) + 32)
# 50.0
