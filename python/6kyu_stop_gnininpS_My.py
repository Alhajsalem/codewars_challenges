#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    result = []
    for item in sentence.split(" "):
        if len(item) >= 5:
            result.append(item[::-1])
        else:
            result.append(item)

    return " ".join(result)
    
spin_words("Hey fellow warriors")


# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    return "{} {}".format(str(max([int(i) for i in numbers.split(" ")])),str(min([int(i) for i in numbers.split(" ")])))


high_and_low("1 2 3 4 5")  # return "5 1"


# https://www.codewars.com/kata/59f4a0acbee84576800000af

from statistics import mean
from itertools import combinations

def pos_average(s):
    return mean(a == b for combo in combinations(s.split(', '), 2) for a, b in zip(*combo)) * 100.



from calendar import weekday, day_name
def most_frequent_days(year):
    return [ day_name[day] for day in sorted( {weekday(year, 1, 1), weekday(year, 12, 31)} ) ]
print(most_frequent_days(1984))

def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0