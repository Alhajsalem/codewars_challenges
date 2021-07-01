# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
# ALGORITHMS STRINGS PERFORMANCE OPTIMIZATION COUNTER 

from collections import Counter

def scramble(s1,s2):
    c_1 = Counter(s1)
    c_1.subtract(Counter(s2))
    return True if len([item for item in c_1.values() if item < 0 ]) == 0 else False

assert scramble('rkqodlw', 'world') ==  True
assert scramble('cedewaraaossoqqyt', 'codewars') == True
assert scramble('katas', 'steak') == False
assert scramble('scriptjava', 'javascript') == True
assert scramble('scriptjavx', 'javascript') == False


# better solution
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

import re
def string_transformer(s):
    result_array = reversed(re.split(r'(\s+)', s))
    result = []
    for i in result_array:
        for letter in i:
            if letter.capitalize() == letter:
                result.append(letter.lower())
            else:
                result.append(letter.capitalize())
    return ("".join(result))

string_transformer("You Know When  THAT  Hotline Bling")#, "bLING hOTLINE  that  wHEN kNOW yOU")

def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])