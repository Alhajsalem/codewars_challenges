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
print(corner_fill(x))

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

print(foo())#, True)
print(bar())#, False)