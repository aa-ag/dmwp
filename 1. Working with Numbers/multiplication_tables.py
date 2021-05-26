def multiplication_table(n, m):
    '''
     multiplication table printer
    '''
    for i in range(1, m + 1):
        print('{0} x {1} = {2}'.format(n, i, n*i))


if __name__ == '__main__':
    while True:
        n = input('Enter a number: ')
        if n == 'q':
            print('bye')
            break

        m = input('Enter a multiple: ')
        if m == 'q':
            print('bye')
            break

        multiplication_table(int(n), int(m))
