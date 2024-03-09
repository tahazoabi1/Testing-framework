from dictKeyCheck import keyDictCheck
from dictValueCheck import dictValCheck
from mathematical import mathcheck
from nestedlistcheck import nestedListCheck


nes_list = [1, 2 ,3, [4, 5, 6], 7]
dict1 = {'aa': {'a': 1, 'b': 2, 'c':3}, 'bb': 4, 'vv': 5}
keyDictCheck(dict1, 'a')
dictValCheck(dict1, '1')
mathcheck(2, 3)
nestedListCheck(nes_list, 5)

