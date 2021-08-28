def true_and_false(true, false):
    print('True & False')
    print('-----------')
    print('True =', true)
    print('False =', false)
    print('----------------------------------')


def logical_not(true, false):
    print('Logical NOT')
    print('-----------')
    print('not True =', not true)
    print('not False =', not false)
    print('----------------------------------')


def logical_and(true, false):
    print('Logical AND')
    print('-----------')
    print('True and True =', true and true)
    print('True and False =', true and false)
    print('False and True =', false and true)
    print('False and False =', false and false)
    print('----------------------------------')


def logical_or(true, false):
    print('Logical OR')
    print('-----------')
    print('True and True =', true or true)
    print('True and False =', true or false)
    print('False and True =', false or true)
    print('False and False =', false or false)
    print('----------------------------------')


def expression():
    print('Expression not(p or not q)')
    print('-----------')
    print('p = True, q = True')
    p = True
    q = True
    print(' not(p or not q) = ', not(p or not q))
    print('p = True, q = False')
    p = True
    q = False
    print(' not(p or not q) =', not (p or not q))
    print('p = False, q = True')
    p = False
    q = True
    print(' not(p or not q) =', not (p or not q))
    print('p = False, q = False')
    p = False
    q = False
    print(' not(p or not q) =', not (p or not q))
    print('----------------------------------')


if __name__ == '__main__':
    TRUE = True
    FALSE = False
    true_and_false(TRUE, FALSE)
    logical_not(TRUE, FALSE)
    logical_and(TRUE, FALSE)
    logical_or(TRUE, FALSE)
    expression()