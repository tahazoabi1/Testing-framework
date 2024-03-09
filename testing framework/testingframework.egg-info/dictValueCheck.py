def dictValCheck(dict1, value):
    print(f'dict val check starting - checking {value} as value')
    for key, val in dict1.items():
        if val == value:
            print('The value is in the dict')
        elif isinstance(val, dict):
            if value in val.values():
                print('The value is in a nested dict')
    print('Its not in the dict or in any nested dict')