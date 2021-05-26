############------------ IMPORTS ------------############
import matplotlib.pyplot as plt


############------------ FUNCTIONS ------------############
def create_graph():
    '''
     savefig before show()
     https://stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image
    '''
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]

    plt.plot(x_numbers, y_numbers)
    plt.savefig('test.png')
    plt.show()


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    create_graph()
