# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python


def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)
    
print(find_missing([-1, 2, 8, 11, 14, 17, 20, 23, 26]))