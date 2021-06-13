#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS
def dig_pow(n, p):
    k = sum([int(item)**(p+index) for index,item in enumerate(str(n))])/n
    return k if k-int(k) == 0 else -1 
    
assert (dig_pow(46288, 3)) ==  51
assert (dig_pow(46288, 5)) ==  -1

# better solution 
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k

# https://www.codewars.com/kata/5848565e273af816fb000449/train/python

import re
def encrypt_this(text):
    return re.sub(r'\b(\w)(\w?)(\w*?)(\w?)\b', lambda m: '{}'.format(str(ord(m.group(1))) + m.group(4) + m.group(3) + m.group(2)), text).replace('   ', ' ').replace('  ', ' ')


print(encrypt_this("A wise old owl lived in an oak"))

def sort_array(source_array):
   print(list(filter(lambda x: x < 20, sorted(source_array, key = lambda x: len(str(x))))))


   odd = sorted(list(filter(lambda x: x % 2, source_array)))
   result = []
   i = 0
   for s in source_array:
       if s % 2 != 0:
           result.append(odd[i])
           i = i +1

       else:
           result.append(s)
   return result
print(sort_array([523444, 344, 2344, 844, 14, 4]))#, [1, 3, 2, 8, 5, 4])


def fn(x):
    return len(x)