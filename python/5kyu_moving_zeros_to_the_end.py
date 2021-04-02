# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# ALGORITHMS INTERVIEW QUESTIONS ARRAYS SORTING

def move_zeros(array):
    x = list(("".join([str(item) for item in array])).replace("0","")+"0"*array.count(0))
    return [int(item) for item in x]

assert move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# better solution 
def move_zeros_1(array):
    return sorted(array, key= lambda x: x == 0, reverse=False)

assert move_zeros_1([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]