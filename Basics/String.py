def string_simple_examples():
    string1 = 'Hello world!'
    string2 = "Hello world!"
    print(string1)
    print(string2)
    # multiline strings use triple quotes
    lorem_ipsum = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pulvinar ac nulla ac elementum. 
    Phasellus at fermentum nibh. Nulla ornare mauris urna, vitae euismod arcu vestibulum ultrices.
    Mauris eget leo feugiat, dignissim est in, tincidunt velit. Mauris imperdiet metus in luctus dignissim. 
    Pellentesque fermentum odio et cursus iaculis. Morbi id tortor ac turpis pharetra tempus. 
    Fusce vitae ultrices quam. Etiam gravida sagittis dolor sit amet finibus.
    '''
    print('=================')
    print(lorem_ipsum)
    print('=================')

    # characters
    chars = 'abc"DEF*&$!@'
    chars2 = "\t'abc'\ndef\'"
    print(chars)
    print(chars2)
    print('=================')


def concatenating_and_repeating_string():
    print('Concatenating')
    cat = 'cat'
    dog = 'dog'
    cat_and_dog = cat + ' and ' + dog
    print(cat_and_dog)
    print('=================')
    print('Repeating')
    lots_of_cats = cat * 10
    print(lots_of_cats)
    print('=================')


def using_str():
    num = 10.25
    str_num = str(num)
    print('number = ' + str_num)
    # wrong:
    # print('number = ' + num)
    print('=================')


def indexing():
    print('Indexing')
    phrase = 'Hello world!'
    print(phrase)
    # first character
    first = phrase[0]
    print(first)
    # 4th character
    fourth = phrase[3]
    print(fourth)
    print('=================')

    # checking type of variable
    print(type(phrase))
    print(type(fourth))
    print('=================')

    # length of string
    phrase_len = len(phrase)
    print(phrase_len)
    # last character
    print(phrase[phrase_len - 1])
    print(phrase[-1])
    # 10th from last character ( 3rd character - 'l')
    print(phrase[-10])
    print('=================')
    # Indices
    # string = 'abcde'
    # character     a   b   c   d   e
    # pos index     0   1   2   3   4
    # neg index    -5  -4  -3  -2  -1


def searching_strings():
    print('Searching strings')
    sentence = 'Lorem ipsum.' + \
        'Lorem ipsum dolor sit amet,' + \
        'consectetur adipiscing elit.' + \
        'Vivamus pulvinar ac nulla ac elementum.'

    # finding strings within strings
    print('Finding ipsum')
    first_ipsum = sentence.find('ipsum')
    print(first_ipsum, sentence[first_ipsum])
    last_ipsum = sentence.rfind('ipsum')
    print(last_ipsum, sentence[last_ipsum])
    print('=================')

    print('Finding Lorem')
    first_lorem = sentence.index('Lorem')
    print(first_lorem, sentence[first_lorem])
    last_lorem = sentence.rindex('Lorem')
    print(last_lorem, sentence[last_lorem])
    print('=================')

    print('Finding pokemon')
    first_pokemon = sentence.find('pokemon')
    print(first_pokemon, sentence[first_pokemon])
    # Error
    # first_pokemon2 = sentence.index('pokemon')
    # print(first_pokemon2, sentence[first_pokemon2])
    print('=================')

    print('Counting strings within strings')
    print('Number of ipsum: ', sentence.count('ipsum'))
    print('Number of Lorem: ', sentence.count('Lorem'))
    print('Number of dolor: ', sentence.count('dolor'))
    print('Number of pokemon: ', sentence.count('pokemon'))
    print('=================')


def slicing():
    word = 'nothing'
    print(word)
    print('=================')
    # selecting substrings
    print('Selecting substrings')
    print(word[1:5])    # output: othi
    print(word[5:7])    # output: ng
    print('=================')

    # open ended slices
    print('Open ended slices')
    print(word[1:])     # output: othing
    print(word[:5])     # output: nothi
    print('=================')

    # negative indices
    print('Negative indices')
    print(word[-4:])     # output: hing
    print(word[1:-4])     # output: ot
    print('=================')

    # indexing past the end
    print('Indexing past the end')
    print(word[8:25])                   # output:
    print('$' + word[22:30] + '@')      # output: $@
    print('=================')

    # empty slices
    print('Counting strings within strings')
    print(word[7:7])     # output:
    print(word[4:1])     # output:
    print('=================')


if __name__ == '__main__':
    string_simple_examples()
    concatenating_and_repeating_string()
    using_str()
    indexing()
    searching_strings()
    slicing()

