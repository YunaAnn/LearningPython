def pythagorean_theorem():
    # a^2+b^2=c^2
    print('Pythagorean Theorem')
    print('the square of the hypotenuse of a right triangle is equal to the sum of the squares of the other two sides')
    # ex -> a = 3, b = 4, c = 5
    try:
        a = float(input('Enter a: '))
        b = float(input('Enter b: '))
        c = float(input('Enter c: '))
        print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
        print('a^2 + b^2 = ', a**2 + b**2)
        print('c^2 = ', c**2)
        if a**2 + b**2 == c**2:
            print('True')
        else:
            print('False')
    except ValueError:
        print('Oops! These were no valid numbers. Try again...')


if __name__ == '__main__':
    pythagorean_theorem()
input('Press Enter to continue...')