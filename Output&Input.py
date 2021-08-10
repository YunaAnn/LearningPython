import math

def print_hi(name):
    print(f'Hello {name}')

def print_pi_value():
    print('pi =',math.pi)

def print_sep():
    print(1,2,3,4,5)
    print(1,2,3,4,5,sep='*')
    print(1,2,3,4,5,sep='*',end='$')
    print(end='\n')

def output_format():
    print('I love {0} and {1}'.format('trains','pancakes'))
    print('I love {1} and {0}'.format('trains','pancakes'))
    x=5; y=7
    print('The value of x is {} and y is {}'.format(x,y))

def input_num():
    num = input('Enter a number: ')
    print('input data - string type ',num)
    print('converted - int {0} and float {1}'.format(int(num),float(num)))
    expression = input('Enter expression (ex. 2+2) ')
    print('Used eval() to evaluate: {0} = {1}'.format(expression, eval(expression)))

if __name__ == '__main__':
    print_hi('User!')
    print_pi_value()
    print_sep()
    output_format()
    input_num()