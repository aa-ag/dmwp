def multiplication_table(a):
    '''
     multiplication table printer
    '''
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))


if __name__ == '__main__':
    while True:
        a = input('Enter a number: ')
        if a == 'q':
            print('bye')
            break
        multiplication_table(int(a))
