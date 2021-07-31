def remove_exclamation_marks(s):
    return s.replace("!","")
remove_exclamation_marks("Hello World!"), "Hello World"


def pipe_fix(nums):
    return [i for i in range(min(nums),max(nums)+1)]

pipe_fix([1, 2, 3, 5, 6, 8, 9])


def validate(n):
    arr_result_1= []
    for i in range(0,len(str(n)),1):
        if i %2 == 0:
            arr_result_1.append(int(str(n)[i])*2)
        else:
            arr_result_1.append(int(str(n)[i]))

    arr_result_2 = []
    for i in arr_result_1:
        if i > 9:
            arr_result_2.append(int(str(i)[0])+ int(str(i)[1]))
        else:
            arr_result_2.append(i)
    return sum(arr_result_2) % 10 == 0
     
def validate(n):
    digits = [int(x) for x in str(n)]
    print(digits[-2::-2])
    even = [x*2 if x*2 <= 9 else x*2 - 9 for x in digits[-2::-2]]
    odd  = [x for x in digits[-1::-2]]
    return (sum(even + odd)%10) == 0


validate(1230)

def clean_string(s):
    if s.find("#") == -1: return s
    s = list(s)
    i = 0
    while i < len(s):
        if s[i] == "#" and i == 0:
            s.pop(i)
            i = i - 1
        elif s[i] == "#" and i != 0:
            s.pop(i)
            s.pop(i-1)
            i = i - 2
        i+=1
    return("".join(s))


print(clean_string("22###(")) # '' should equal '7&'

def clean_string_1(s):
    l = []
    for x in s:
        if x != "#": 
            l.append(x)
        elif len(l) > 0:
            l.pop()
    return ''.join(l)
    
print(clean_string_1("22###("))

import re
def sum_arrays(array1,array2):
    if len(array1) == 0: return array2
    if len(array2) == 0: return array1
    x = int("".join([str(i) for i in array1]))+int("".join([str(i) for i in array2]))
    if str(x).find("-") == -1:
        return [int(i) for i in str(x)]
    else:
        y = [int(item)*-1 if index == 0 else int(item) for index,item in enumerate(str(x)[1:])]
        if y[0] == 0:
            return y[1:0]
        else:
            return y
print(sum_arrays([0,4],[]))#,[2])

def count_adjacent_pairs(st):
    result = [None]
    array_str= st.lower().split(" ")
    for i in range(len(array_str)-1):
        if array_str[i] == array_str[i+1] and array_str[i+1] != result[-1]:
            result.append(array_str[i+1])
    return len(result)-1

count_adjacent_pairs('HEx hEX zip zip zIp dIcT repR RePR Ord Ord orD iteR stAticmeThod loCALs lOcALS LOcaLs lOCaLs issuBClaSs iSSUbcLasS isSubClASs iSsUbcLass ZIp ZIp')#, 1)


#['hex', 'zip', 'repr', 'ord', 'locals', 'issubclass']
['hex', 'zip', 'repr', 'ord', 'locals', 'issubclass', 'zip']

from itertools import groupby
def count_adjacent_pairs(st): 
    return len([name for name,group in groupby(st.lower().split(' ')) if len(list(group))>=2])

count_adjacent_pairs('HEx hEX zip zip zIp dIcT repR RePR Ord Ord orD iteR stAticmeThod loCALs lOcALS LOcaLs lOCaLs issuBClaSs iSSUbcLasS isSubClASs iSsUbcLass ZIp ZIp')#, 1)



# https://www.codewars.com/kata/5d774cfde98179002a7cb3c8/train/python
def make_class(*args):
    def wrapper_1 (*values):
        class Myclass:
            def __init__(self):
                for i in range(len(args)):
                    setattr(self, args[i], values[i]) 
        return Myclass()
    return wrapper_1


Animel = make_class("name", "species", "age", "health", "weight", "color")
dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    count = 0
    while len(signature) < n:
        signature.append(sum(signature[count:]))
        count+=1
    return signature[:n]

tribonacci([1, 1, 1], 1)

#https://www.codewars.com/kata/5511b2f550906349a70004e1

import numpy as np 
def last_digit(n1, n2):
    print(np.power(n1,n2))
    
    #print(pow(n1, n2))

last_digit(2 ** 200, 2 ** 300)#, 9)


def create_generator():
    mylist = range(5000)
    for i in mylist:
        yield i


def find_nb(m):
    counter = 0
    result = 0
    while result <= m: 
        result+= (counter) ** 3
        if result == m:
            return counter
        counter+=1
    return -1
print(find_nb(1071225)) #--> 45


def anagrams(word, words):
    result = []
    for word_ in words:
        if "".join(sorted(word)) == "".join(sorted(word_)):
            result.append(word_)
    print(result)


# better solution
def anagrams_1(word, words):
    return [w for w in words if sorted(word)==sorted(w)]


def increment_string(strng):
    n = strng.rstrip('0123456789')
    x = strng[len(n):]
    if len(x) == 0:
        return strng + '1'
    result = 1 + int(x)
    result = str(result).zfill(len(x))
    return n + result

print(increment_string("<7016'u_~2469LX7<9000000401760459"))#, "foobar002")

