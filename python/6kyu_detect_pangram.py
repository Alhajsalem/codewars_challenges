# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
# FUNDAMENTALS STRINGS DATA STRUCTURES

import string

def is_pangram(s):
    letters_as_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    let_array = [letter.capitalize()for letter in s if letter.isalpha()]  
    return True if list(sorted(set(let_array))) == letters_as_array else False

pangram = "The quick, brown fox jumps over the lazy dog!"
assert is_pangram(pangram) == True



#better solution
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())



def beggars(values, n):
    array = []
    for i in range(n):
       array.append(values[i::n])
    array_2 = []
    for i in range(len(array)):
        array_2.append(sum(array[i]))
    return array_2
 


beggars([1,2,3,4,5],3)#,[9,6]

from collections import Counter
def delete_nth(order,max_e):

    print(Counter(order))



delete_nth([20,37,20,21], 1)