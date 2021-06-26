# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
# REGULAR EXPRESSIONS
import re

"""
Identifiers
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""

#matches = re.findall(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}', sentence)

#regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$'


from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)
import string
def pig_it(text):
    array = []
    text_array = text.split(" ")
    for world in text_array:
        if world in string.punctuation:
            array.append(world)
        else:
            array.append(world[1:]+world[0]+"ay")

    return " ".join(array)



pig_it('Hello world !')#,'igPay atinlay siay oolcay'

def row_sum_odd_numbers(n):
    array = []
    start= n*(n-1)+1
    ende = start + (2*n-1)
    for i in range(start,ende,2):
        array.append(i)   
    return sum(array)


row_sum_odd_numbers(2)