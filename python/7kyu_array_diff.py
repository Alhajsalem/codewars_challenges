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