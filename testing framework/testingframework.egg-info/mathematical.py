
def mathcheck(tested_value, compare_value):
    print(f'Math Check started we comparing {tested_value} to {compare_value}')
    if tested_value > compare_value:
        print(f'{tested_value} bigger than {compare_value}')
        return
    elif tested_value < compare_value:
        print(f'{tested_value} smaller than {compare_value}')
        return
    else:
        print(f'{tested_value} equal to {compare_value}')
        return