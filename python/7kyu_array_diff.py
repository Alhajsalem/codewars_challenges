# FUNDAMENTALS ARRAYS

# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    return [a[i] for i in range(len(a)) if a[i] not in b]
        
assert array_diff([1,2], [1]) ==  [2], "expected results [2]"

#better solution 
def array_diff(a, b):
    return [x for x in a if x not in b]


def maskify(cc):
    counter = 0
    arr = []
    for i in range(len(cc)-1,-1,-1):
        if counter < 4:
            counter += 1
            arr.append(cc[i])
        else:
            arr.append('#')
    return "".join(list(reversed(arr)))
maskify("Nananananananananananananananana Batman!")


def maskify_1(cc):
    return "#"*(len(cc)-4) + cc[-4:]

maskify_1("Nananananananananananananananana Batman!")

# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

from collections import Counter
def combine(*args):
    arr = []
    for i in range(len(args)):
        arr.append(Counter(args[i]))
    n = Counter()
    for i in range(len(arr)):
         n = n + arr[i]
    return dict(n)


objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
objC = { 'a': 5, 'd': 11, 'e': 8 }
objD = { 'c': 3 }

combine(objA, objB, objC) # Returns { a: 13, b: 20, c: 36, d: 3 }

# better solution
from collections import Counter
def combine(*dc):
    c = Counter()
    for d in dc:
        c.update(d)
    return c



def duplicate_count(text):
    arr = [letter.capitalize() for letter in text]
    x = list(set(arr))
    y = "".join(arr)
    count = 0
    for i in x:
        if y.count(i) > 1:
            count += 1 
    return count

duplicate_count("indivisibility")

def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count



def duplicate_encode(word):
    result = ""
    for letter in word.lower():
        if word.lower().count(letter) > 1:
            result += ")"
        else:
           result += "("
    return result
duplicate_encode("(( @")#,"()()()"

g = lambda a, b : a *b 

print(g(2,2))
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

import itertools
def get_pins(observed):
    rules = {"1": [1,2,4],"2": [1,2,3,5], "3" :[2,3,6],
    "4" : [1,4,5,7], "5" : [2,4,5,6,8],  "6": [3,5,6,9],
    "7" : [4,7,8], "8" : [5,7,8,9,0], "9" : [6,8,9], "0" : [0,8]}
    search = []
    for i in str(observed):
        search.append(rules[i])
    return ([''.join(map(str,num)) for num in [list(w) for w in itertools.product(*search)]])
  


def friend(x):
    return list(filter(lambda name: len(name) == 4, x))


friend(["Ryan", "Kieran", "Mark",])#, ["Ryan", "Mark"]


def remove_smallest(numbers):
    new_list = numbers.copy()
    if len(new_list) == 0: return []
    del new_list[new_list.index(min(new_list))]
    return new_list


print(remove_smallest([1, 2, 3, 4, 5]))#, [2, 3, 4, 5],

def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2


print(find_next_square(625))#, 144, "Wrong output for 121")