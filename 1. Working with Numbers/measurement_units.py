def print_menu():
    print('Enter 1 to convert kilometers to miles\n2 to convert miles to kilometers\n"q" to quit\exit')


def kilometer_to_miles():
    kilometers = input('Enter number of kilometers:\n')
    return f"\n{kilometers} kilometers equals {round(int(kilometers) / 1.609, 2)} miles."


def miles_to_kilometers():
    miles = input('Enter number of miles:\n')
    return f"\n{miles} miles equals {round(int(miles) * 1.609, 2)} kilometers."


if __name__ == '__main__':
    print_menu()

    while True:
        option = input('\nWhich conversion would you like to do?\n')

        if option == 'q':
            print('\nbye.')
            break

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
