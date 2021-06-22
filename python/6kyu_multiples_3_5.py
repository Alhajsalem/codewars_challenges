# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
#ALGORITHMS MATHEMATICS NUMBERS

def solution(number):
    arr = []
    for i in range(1,number):
        x_3,y_3 = divmod(i,3)
        x_5,y_5 = divmod(i,5)
        if y_3 == 0 or y_5 ==0:
            arr.append(i)
    return sum(arr)


assert solution(10) == 23

# better solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def multiplication_table(row,col):
    arr = []
    for i in range(1,row+1):
        x = []
        for j in range(1,col+1):
            x.append(j*i)
        arr.append(x)
    return arr
multiplication_table(3,3)#, [[1,2,3],[2,4,6],[3,6,9]])
multiplication_table(3,4)#, [[1,2,3,4],[2,4,6,8],[3,6,9,12]])

def reverse_words(text):

  return " ".join([i[::-1] for i in text.split(" ")])

import math
def find_squares(num):
    array = create_generator()
    x = [0]
    for i,k in enumerate(array):
        x.append(k)
        if x[i+1] - x[i] == num:
            return "{}-{}".format(x[i+1], x[i])

def create_generator():
    mylist = range(1000000)
    for i in mylist:
        yield i*i

print(find_squares(7*9))