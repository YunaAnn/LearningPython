def numeric_literals():
    binary = 0b1010
    decimal = 100
    octal = 0o310
    hexadecimal = 0x12c
    float1 = 2.5
    float2 = 2.5e2
    complex = 1.23j
    print('Numeric literals')
    print(binary, decimal, octal, hexadecimal)
    print(float1, float2)
    print(complex, complex.imag, complex.real)

def string_literals():
    string = 'Hello world!'
    char = 'A'
    multiline_string = '''This is a multiline string with more than one line code. aaaaaaaaaaaaaaaaaaa. rgrsggsdhfdhgffasfhgredcsvrdyhdhfdreyhhd'''
    unicode = u'\u00dcnic\u00f6de'
    print('String literals')
    print('string: ', string)
    print('char:', char)
    print('multiline: ', multiline_string)
    print('unicode: ', unicode)

def boolean_literals():
    x = (1 == True)
    y = (1 == False)
    a = True + 1
    b = False + 1
    print('Boolean literals')
    print('x is {0}, y is {1}'.format(x, y))
    print('a: {0}, b: {1}'.format(a, b))

if __name__ == '__main__':
    numeric_literals()
    string_literals()
    boolean_literals()