# FUNDAMENTALS ARRAYS

# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    return [a[i] for i in range(len(a)) if a[i] not in b]
        
assert array_diff([1,2], [1]) ==  [2], "expected results [2]"

#better solution 
def array_diff(a, b):
    return [x for x in a if x not in b]