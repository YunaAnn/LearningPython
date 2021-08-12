def while_loop():
    cycle = 1
    print('While loop: ')
    while cycle < 6:
        print('Inside a loop -> cycle : ', cycle)
        cycle = cycle + 1
    print('Done - cycle =', cycle)

def multiplication_table():
    print(' -------------------- ')
    print('Multiplication table: ')
    number = 1; count = 1
    while count <= 10:
        result = count * number
        print('{0} * {1} = {2}'.format(number,count,result))
        count = count + 1

def countdown():
    print(' -------------------- ')
    print('Countdown :')
    count = 10
    while count >= 0:
        print(count)
        count = count - 1
    print ('Booooooooooom')

def add_natural():
    print(' -------------------- ')
    # sum = 1+2+3+...+n
    sum = 0
    n = 10
    i = 0
    while n >= 0:
        sum = sum + i
        i = i + 1
        n = n - 1
    print (' sum = 1 + 2 + 3 + ... + n ')
    print (' n = 10 => 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 =', sum)

def loop_with_else():
    print(' -------------------- ')
    print('While loop with else')
    count = 0
    while count < 5:
        print ('Inside while loop. condition -> count < 5.')
        print ('count = ', count)
        count = count + 1
    else:
        print ('Inside else.')
        print('count = ', count)


if __name__ == '__main__':
    while_loop()
    multiplication_table()
    countdown()
    add_natural()
    loop_with_else()

