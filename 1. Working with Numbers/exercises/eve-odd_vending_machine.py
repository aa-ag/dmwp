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

        if int(n) % 2 == 0:
            print(f"\n{n} is even")
        else:
            print(f"\n{n} is odd")


######------ DRIVER CODE ------######
if __name__ == '__main__':
    even_odd_vending_machine()
