def list_literals():
    print('List Literals')
    print('----')

    empty_list = []
    numbers_list = [3, 4, 8, 6, 1, 9, 2, 7]
    letters_list = ['a', 'b', 'c', 'd', 'e']
    programming_languages = ['Python', 'Java', 'JavaScript', 'C#']
    # better not to mix types
    mixed_list = [1, 'z', False]

    print(empty_list)
    print(numbers_list)
    print(letters_list)
    print(programming_languages)
    print(mixed_list)

    print('---------------------------------------')


def creating_lists():
    print('Creating Lists')
    print('----')

    my_list = list()
    print(my_list)

    seq = range(10)
    seq_list = list(seq)
    seq2 = range(4, 7)
    seq3 = range(10, 100, 10)
    seq4 = range(10, 0, -1)
    print(seq)
    print(seq_list)
    print(seq2, list(seq2))
    print(seq3, list(seq3))
    print(seq4, list(seq4))

    print('---------------------------------------')


def list_indexing():
    print('List Indexing')
    print('----')

    fruit = ['apple', 'banana', 'orange', 'blueberry', 'watermelon']
    print(fruit)

    print(fruit[0])                         # 1st item, output: apple
    print(fruit[2])                         # 3rd item, output: orange
    print(fruit[-1])                        # last item, output: watermelon
    print(fruit[-4])                        # 4th from last item, output: banana

    length_of_list = len(fruit)             # length of list / number of items
    print(length_of_list)                   # output: 5
    print(fruit[length_of_list - 1])        # last item, output: watermelon

    print('---------------------------------------')

    # Indices
    # list = [4, 7, 2, 3, 6, 1, 9 ,8]
    # item          4   7   2   3   6   1   9   8
    # pos index     0   1   2   3   4   5   6   7
    # neg index    -8  -7  -6  -5  -4  -3  -2  -1


def list_slicing():
    print('List Slicing')
    print('----')

    numbers = list(range(0, 101, 10))
    print(numbers)

    print(numbers[2:3])         # sublists
    print(numbers[4:7])

    print(numbers[2:])         # open ended slices
    print(numbers[:7])

    print(numbers[-2:])         # negative indices
    print(numbers[1: -4])

    print(numbers[4:1])         # empty slices
    print(numbers[11:13])

    print('---------------------------------------')


def list_searching():
    print('List Searching')
    print('----')

    vegetables = ['onion', 'carrot', 'tomato', 'potato', 'pepper', 'cucumber']
    print(vegetables)
    print('----')
    print('Finding items in the list (index)')
    # finding items in the list (index)
    print(vegetables.index('potato'))       # output: 3
    print(vegetables.index('tomato'))       # output: 2
    # print(vegetables.index('apple'))      # not in the list - output:
    print('----')
    print('Checking if items are in a list')
    print('tomato' in vegetables)
    print('onion' in vegetables)
    print('apple' in vegetables)
    print('tomato' not in vegetables)
    print('apple' not in vegetables)
    print('----')
    print('Counting items in list')
    print(vegetables.count('carrot'))
    print(vegetables.count('apple'))
    print('---------------------------------------')


def iterating_over_lists():
    print('Iterating over lists')
    print('----')
    print('iterate over list print all items')
    print('----')
    languages = ['Python', 'Java', 'JavaScript', 'C#']
    numbers = list(range(5, 21, 5))
    print(languages)
    print(numbers)
    for item in languages:
        print(item)
    for item in numbers:
        print(item)
    print('----')
    
    print('Counting number of items in a list')
    print('----')
    # count number of items in a list
    count = 0
    for item in languages:
        count = count + 1
    print(count)
    print('---------------------------------------')

if __name__ == '__main__':
    list_literals()
    creating_lists()
    list_indexing()
    list_slicing()
    list_searching()
    iterating_over_lists()


