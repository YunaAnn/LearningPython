def capital_indexes(string):
    indexes = []
    for i in range(len(string)):
        if string[i].isupper():
            indexes.append(i)
    return indexes


if __name__ == '__main__':
    print(capital_indexes('HeLlO'))
    