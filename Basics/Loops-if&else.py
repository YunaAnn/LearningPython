import math


def quadratic_equation():
    # if, elif, else
    print('''quadratic equation: x^2 + 3x - 4 = 0''')
    a = 1
    b = 3
    c = -4
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
    delta = (-b) ** 2 - 4 * a * c
    print('delta =', delta)
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        print('x1 = {0}, x2 = {1}'.format(x1, x2))
    elif delta == 0:
        x0 = -b / (2 * a)
        print('x0 = ', x0)
    else:
        print('delta < 0 - no real roots')


def check_if_number_is_positive_negative_or_zero():
    # nested if + input float type ex
    number = float(input('Enter a number: '))
    if number >= 0:
        if number == 0:
            print('Zero')
        else:
            print('Positive number')
    else:
        print('Negative number')


if __name__ == '__main__':
    quadratic_equation()
    check_if_number_is_positive_negative_or_zero()
