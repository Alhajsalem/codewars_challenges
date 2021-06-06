# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
# FUNDAMENTALS LISTS DATASTRUCTURES FILTERING
def filter_list(l):
  return [item for item in l if type(item) == int]
assert filter_list([1,2,'a','b']) == [1,2]


def square_digits(num):
    return int("".join([str(pow(int(i),2)) for i in str(num)]))
square_digits(9119)


def song_decoder(song):
    print(" ".join(song.split("WUB")).strip().replace("  "," ").replace("  "," "))

song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND


def song_decoder(song):
    """ Simple WUB decoder :) """
    x = list(filter(lambda x: x != '', song.split('WUB')))

    return ' '.join(x)
song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB")
