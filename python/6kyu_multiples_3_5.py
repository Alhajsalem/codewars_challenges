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