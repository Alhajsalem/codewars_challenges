
def reverse_alternate(string):
    result = []
    for index,item in enumerate(string.split()):
        if index %2 != 0:
            result.append(item[::-1])
        else:
            result.append(item)
    
    return " ".join(result)


reverse_alternate("This       is a  test ")

import numpy as np
def matrix_addition(a, b):
    x = (np.add(a,b)).tolist()
    return x

import string

def rot13(message):
     x = string.ascii_lowercase
     y = string.ascii_uppercase
     result = []
     for letter in message:
         if letter.islower():
            result.append(x[(x.index(letter)+13) % len(x)])
         elif letter.isupper():
            result.append(y[(y.index(letter)+13) % len(y)])
         else:
            result.append(letter)

     return ("".join(result))


rot13("test")#,"grfg")
rot13("Test")#,"Grfg")
from collections import Counter
from collections import defaultdict
def mix(s1, s2):
    x = Counter(s1.replace(" ", ""))
    y = Counter(s2.replace(" ", ""))
    result = dict(sorted((x | y).items(), key=lambda x: x[1], reverse=True))
    points_small = dict(filter(lambda x: x[1] > 1 and x[0].islower() , result.items()))
    points_small = dict(sorted(list(points_small.items()), key=lambda t: (-1*t[1], t[0])))
    print(points_small)
    new_dict = {}
    for k, v in points_small.items():
         new_dict.setdefault(v, []).append(k)
    print(new_dict)
    x = dict(x)
    y = dict(y)
    result_finall = []
    for i in points_small.items():
        if i in x.items() and i in y.items():
            result_finall.append("=:{}".format(i[0]*i[1]))
        elif i in x.items():
            result_finall.append("1:{}".format(i[0]*i[1]))
        elif i in y.items():
            result_finall.append("2:{}".format(i[0]*i[1]))
    return("/".join(result_finall))


mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp")
# 2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')

def sum_array(arr):
    if len(arr) < 3 or arr ==None: return 0
    return sum(sorted(arr)[1:-1])


sum_array([6, 2, 1, 8, 10])#, 16