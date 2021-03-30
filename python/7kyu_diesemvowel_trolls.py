# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
# FUNDAMENTALS STRINGS REGULAREXPRESSIONS DECLARATIVEPROGRAMMING ADVANCED LANGUAGE FEATURES
import re
def disemvowel(string):
    result = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    return result

assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"

# solution without using re

def disemvowel_1(s):
    vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
    str = ""
    for letter in s:
        if letter in vowels:
            s.replace(letter,"")
        else:
            str += letter
    return str
assert disemvowel_1("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"

# better solution 
def disemvowel_2(s):
    return s.translate(str.maketrans('','','aeiouAEIOU'))
   
assert disemvowel_2("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"