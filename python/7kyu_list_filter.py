# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
# FUNDAMENTALS LISTS DATASTRUCTURES FILTERING
def filter_list(l):
  return [item for item in l if type(item) == int]
assert filter_list([1,2,'a','b']) == [1,2]


def square_digits(num):
    return int("".join([str(pow(int(i),2)) for i in str(num)]))
square_digits(9119)


def song_decoder(song):
    return (" ".join(song.split("WUB")).strip().replace("  "," ").replace("  "," "))

song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB")


def song_decoder(song):
    """ Simple WUB decoder :) """
    x = list(filter(lambda x: x != '', song.split('WUB')))

    return ' '.join(x)
song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB")


def corner_fill(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + [row.pop(-1) for row in array][::-1]
        res = res + array.pop(0)[::-1]
    return res if not array else res + array[0]

x = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
corner_fill(x)

import time
def timer(limit):
    def wrapper_1(fn):
        def wrapper_2(*args):
            time_now = time.time()
            fn(*args)
            total_secs = round(time.time() - time_now)
            return total_secs < limit    
        return wrapper_2
    return wrapper_1

from time import sleep

@timer(10)
def foo():
    sleep(0.1)
 
@timer(1)
def bar():
    sleep(1.1)

#print(foo())#, True)
#print(bar())#, False)

class UnexpectedTypeException(Exception):
    pass
def expected_type(return_types):
    def wrapper_1(fn):
        def wrapper_2(*args):
            if isinstance(fn(*args), return_types):
                return fn(*args)
            else:
                raise UnexpectedTypeException("the type not matching")
        return wrapper_2
    return wrapper_1

@expected_type((str,))
def return_something(something):
    return something


return_something('The quick brown fox jumps over the lazy dog.')

def alphanumeric(string):
    return string.isalnum()

print(alphanumeric("helloworld_"))

def double_char(s):
    return "".join([le+le for le in s])

print(double_char("String")) #==> "SSttrriinngg"

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


gimme([2, 3, 1])#, 0, 

def remove_duplicate_words(s):
    return " ".join((sorted(set(s.split(" ")), key=s.split(" ").index)))

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
#, "alpha beta gamma delta")

def to_csv_text(array) :
    return(str(array).replace('],', '\n').replace('[', '').replace(']', '').replace(' ', '')) 

print(to_csv_text([
            [5, 55, 5, 5, 55],
            [6, 6, 66, 23, 24],
            [666, 31, 66, 33, 7]
        ]))