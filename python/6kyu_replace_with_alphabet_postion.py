# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
# FUNDAMENTALS STRINGS
import string
def alphabet_position(text):
    return " ".join([str(string.ascii_lowercase.find(letter)+1) for letter in text.lower() if letter.isalpha()])
assert alphabet_position("The sunset sets at twelve o' clock.") ==  "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
assert alphabet_position("The narwhal bacons at midnight.") ==  "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"


# better solution 
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
