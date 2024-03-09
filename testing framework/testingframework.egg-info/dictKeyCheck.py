
def keyDictCheck(dict1, key):
    print(f'key check starting - checking {key} as key')
    if key in dict1:
        print('The key is in the dict.')
        return
    for value in dict1.values():
        if isinstance(value, dict):
            if key in value:
                print('The key is in a nested dictionary.')
                return
    print('the key is not In dict or in Nested dict')
    return