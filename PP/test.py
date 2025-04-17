
def rek(n, start, goal, additional):
    if n > 0:
        #print('rek ', n, start, goal, additional, end=' : ')
        rek(n - 1, start, goal, additional)
        print('\n', n, start, additional, end = ' ')
        rek(n - 1, goal, start, additional)
        print('\n', n, additional, goal, end = ' ')
        rek(n - 1, start, goal, additional)




rek(3, 'A', 'C', 'B')
