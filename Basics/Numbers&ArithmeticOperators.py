import math


def numbers():
    print('int')
    print('0 =', 0)
    print('1 =', 1)
    print('-50 =', -50)
    print('3452324353465463634 =', 3452324353465463634)
    print('---------------------')

    print('float')
    print('0.0 =', 0.0)
    print('1.0 =', 1.0)
    print('10.75 =', 10.75)
    print('-100.4 =', -100.4)
    print('---------------------')

    print('Precision')
    print('3.27184736281728392718 =', 3.27184736281728392718)
    print('9.7328294820381903829014021940 =', 9.7328294820381903829014021940)
    print('---------------------')

    print('Scientific notation')
    print('8e44 =', 8e44)
    print('4444444444444444444444444444444.4 =', 4444444444444444444444444444444.4)
    print('---------------------')

    print('Infinity')
    print('1e500 =', 1e500)
    print('-1e500 =', -1e500)
    print('---------------------')

    print('Conversions - numeric types')
    print('float(5) =', float(5))
    print('float(99999999999999999999999999999) =', float(99999999999999999999999999999))
    print('int(5.0) =', int(5.0))
    print('int(8.47) =', int(8.47))
    print('int(-4.9) =', int(-4.9))
    print('---------------------')


def expressions():
    print('Unary operators')
    print('+10 = ', +10)
    print('-77 = ', -77)
    print('+9.133 = ', +9.133)
    print('-16282.79 =', -16282.79)
    print('---------------------')

    print('Addition and Subtraction ( + & - )')
    print('2 + 2 =', 2 + 2)
    print('45 - 77 =', 45 - 77)
    print('3.77 + 1.75 =', 3.77 + 1.75)
    print('5.75 - 2.71 =', 5.75 - 2.71)
    print('3.5 + 4 =', 3.5 + 4)
    print('10 - 2.75 =', 10 - 2.75)
    print('---------------------')

    print('Multiplication ( * )')
    print('2 * 3 =', 2 * 3)
    print('7.5 * 0.25 =', 7.5 * 0.25)
    print('-0.75 * 4 =', -0.75 * 4)
    print('---------------------')

    print('Division and Floor Division ( / & // )')
    print('50 / 10 =', 50 / 10)
    print('3 / 2 =', 3 / 2)
    print('4.128 / 8.24 =', 4.128 / 8.24)
    print('50 // 10 =', 50 // 10)
    print('3 // 2 =', 3 // 2)
    print('4.128 // 8.24 =', 4.128 // 8.24)
    print('---------------------')

    print('Exponentiation ( ** )')
    print('5 ** 3 =', 5 ** 3)
    print('7 ** 2 =', 7 ** 2)
    print('21.4 ** 5 =', 21.4 ** 5)
    print('64 ** 0.5 =', 64 ** 0.5)
    print('---------------------')

    print('Square root (sqrt() + import math module -> math.sqrt())')
    print('math.sqrt(8) = ', math.sqrt(8))
    print('math.sqrt(4) = ', math.sqrt(4))
    print('---------------------')

    print('Modulus ( % )')
    print('5 % 2 =', 5 % 2)
    print('8 % 6 =', 8 % 6)
    print('8 % 4 =', 8 % 4)
    print('21 % 13 =', 21 % 13)
    print('---------------------')


if __name__ == '__main__':
    numbers()
    expressions()
