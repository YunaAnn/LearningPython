
def sum_all_numbers_stored_in_a_list():
    list_of_numbers = [5, 1, 7, 4, 10, 2, 3, 9, 8]
    sum = 0
    for val in list_of_numbers:
        sum = sum + val
    print(5, 1, 7, 4, 10, 2, 3, 9, 8,sep='+')
    print('=', sum)

def range_function():
    print(range(10))
    print(list(range(10)))
    print(list(range(10, 21)))
    print(list(range(0, 100, 10)))

def for_loop_index():
    hobby = ['reading', 'listening to music', 'playing video games', 'watching movies']
    string = ''
    for i in range(len(hobby)):
        print('I like', hobby[i])
    for val in hobby:
        string = string + ' ' + val
        print ('I like', string)

def for_loop_with_else():
    data = [1, 4, 7, 2]
    for i in data:
        print(i)
    else:
        print ('No items left.')

def for_loop_with_else_and_break():
    name = 'Adam'
    age = {'John': 45, 'Eva': 27, 'Liz': 53}
    for person in age:
        if person == name:
            print(age[person])
            break
    else:
        print ('No data found.')
    
if __name__ == '__main__':
    sum_all_numbers_stored_in_a_list()
    range_function()
    for_loop_index()
    for_loop_with_else()
    for_loop_with_else_and_break()
