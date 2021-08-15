def fibonacci_numbers_recursion(n):
    result = 0
    if n == 0:
        return result
    elif n == 1:
        result = 1
        return result
    else:
        result = fibonacci_numbers_recursion(n-1) + fibonacci_numbers_recursion(n-2)
        return result


def fibonacci_numbers_iteration(n):
    f0, f1 = 0, 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for i in range(0, n):
            f0, f1 = f1, f0 + f1
        return f0


if __name__ == '__main__':
    # F0 = 0; F1 = 1
    # Fn = Fn-1 + Fn-2
    print('Fibonacci numbers')
    try:
        n_ = int(input('Enter n:'))
        print('Recursive: F{0} = {1}'.format(n_, fibonacci_numbers_recursion(n_)))
        print('Iterative: F{0} = {1}'.format(n_, fibonacci_numbers_iteration(n_)))
    except ValueError:
        print('Oops! That was no valid number. Try again...')
input("Press enter to continue...")
