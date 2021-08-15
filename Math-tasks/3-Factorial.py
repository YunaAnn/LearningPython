def factorial_recursion(n):
    try:
        if n == 0 or n == 1:
            result = 1
            print('{0}! = {1}'.format(n, result))
        else:
            result = n * factorial_recursion(n - 1)
            print('{0}! = {1}'.format(n, result))
        return result
    except ValueError:
        print('Oops! These were no valid numbers. Try again...')


def factorial_iteration(n):
    try:
        result = 1
        if n == 0 or n == 1:
            print('{0}! = {1}'.format(n, result))
        else:
            for i in range(n, 1, -1):
                result = result * i
            print('{0}! = {1}'.format(n, result))
        return result
    except ValueError:
        print('Oops! These were no valid numbers. Try again...')


if __name__ == '__main__':
    # n! = 1*2*3*...*n
    print('Factorial')
    try:
        n_ = int(input('Enter n = '))
        if n_ >= 0:
            print('Factorial - recursion')
            factorial_recursion(n_)
            print('Factorial - iteration')
            factorial_iteration(n_)
        else:
            print('Enter n >= 0')
    except ValueError:
        print('Oops! That was no valid number. Try again...')
