# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python


def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)
    
find_missing([-1, 2, 8, 11, 14, 17, 20, 23, 26])


def valid_word(seq, word): 
    return not word or any(valid_word(seq,word[len(x):]) for x in seq if word.startswith(x))

valid_word(['code', 'wars'], 'codewars')


def create_multiplications(n):
    return [lambda x : i * x for i in range(n)]

res = [m(3) for m in create_multiplications(3)]
print(res)

#[0,3,6]
#[0,4,8,12]

def get_length_of_missing_array(array_of_arrays):
    if array_of_arrays == []: return 0
    result = sorted([len(x)for x in array_of_arrays])
    for i in [i for i in range(1,max(result)+1)]:
        if i == 0 or i == None: return 0
        if i not in result:
            return i

def get_length_of_missing_array(array_of_arrays):
    print(array_of_arrays)
    if array_of_arrays == []: return 0
    result = sorted([len(x)for x in array_of_arrays])
    for i in [i for i in range(1,max(result)+1)]:
        if i not in result:
            return i

get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]])#, 3)

import re

def top_3_words(text):
    # "'*[a-z][a-z']*"
    result_array = re.findall("[\s]?([']?[A-Za-z]+'?[A-Za-z']*)[\s,:]?", text)
    data = {}
    for i in result_array:
        data[i.lower()] = result_array.count(i)
    data = sorted(data, key=data.get,reverse=True)
    if len(data) >3: return data[0:3]
    if len(data) == 2: return data[0:2]
    if len(data) == 1: return data[0:1]
    return data
print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
#, ["a", "of", "on"]

import re

def is_valid_coordinates(coordinates):
    return bool(re.match("-?(\d|[1-8]\d|90)\.?\d*, -?(\d|[1-9]\d|1[0-7]\d|180)\.?\d*$", coordinates))


]