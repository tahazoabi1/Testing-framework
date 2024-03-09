def nestedListCheck(list1, value):
    print(f'nested list check starting - checking if {value} in a nested list or in a list')

    for i in range(len(list1)):
        if list1[i] == value:
            print(f'{value} found in a List')
        elif isinstance(list1[i], list):
            for j in range(len(list1[i])):
                if list1[i][j] == value:
                    print(f'{value} found in nested list')
                    return

    print('Its not in the list or in any nested list')
    return
