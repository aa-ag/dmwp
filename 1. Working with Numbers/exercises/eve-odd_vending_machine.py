######------ INSTRUCTIONS ------######
'''
Try writing an "even-odd vending machine", 
which will take a number as input and do two things:
(1) Print whether the number is even or odd.
(2) Display the number followed by the next 9 even or odd numbers
'''
######------ SOLUTION ------######
# https://nostarch.com/doingmathwithpython


######------ FUNCTIONS ------######
def even_odd_vending_machine():
    while True:
        n = input("\nEnter an integer (and \"q\" to quit/exit):\n")

        if n == 'q':
            print('\nbye.')
            break

        n = int(n)

        if n % 2 == 0:
            print(f"\n---> {n} is even")
            print(
                f"\nHere's a list with\nthe next 9 even numbers:\n{generate_list(n)}")
        else:
            print(f"\n---> {n} is odd")
            print(
                f"\nHere's a list with\nthe next 9 odd numbers:\n{generate_list(n)}")


def generate_list(n):
    l = []
    while len(l) < 10:
        l.append(n)
        n = n + 2
    return l


######------ DRIVER CODE ------######
if __name__ == '__main__':
    even_odd_vending_machine()
