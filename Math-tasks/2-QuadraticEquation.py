import math


def quadratic_equation():
    try:
        print('''quadratic equation: ax^2 + bx - c = 0''')
        a = float(input('Enter a:'))
        b = float(input('Enter b:'))
        c = float(input('Enter c:'))
        print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
        delta = (-b)**2-4*a*c
        print('delta =', delta)
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / 2 * a
            x2 = (-b + math.sqrt(delta)) / 2 * a
            print('There are 2 roots: x1 = {0}, x2 = {1}'.format(x1, x2))
        elif delta == 0:
            x0 = -b/(2*a)
            print('There is 1 root: x0 = ', x0)
        else:
            print('delta < 0 - no real roots')
    except ValueError:
        print('Oops! These were no valid numbers. Try again... Ex. a = 1, b = 3, c = -4')


if __name__ == '__main__':
    quadratic_equation()
input('Press Enter to continue...')