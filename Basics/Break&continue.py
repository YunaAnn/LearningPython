def break_statement():
    print('Break if "l" -> Hello world!')
    for val in 'Hello world!':
        if val == 'l':
            break
        print(val)
    print('The end.')


def continue_statement():
    print(' ------------------ ')
    print('Continue if "l" -> Hello world!')
    for val in 'Hello world!':
        if val == 'l':
            continue
        print(val)
    print('The end.')


def print_odd_numbers():
    print(' ------------------ ')
    numbers = list(range(1, 21))
    print('All numbers: ', numbers)
    print('Odd numbers: ')
    for val in numbers:
        if val % 2 == 0:
            continue
        print(val)


if __name__ == '__main__':
    break_statement()
    continue_statement()
    print_odd_numbers()
