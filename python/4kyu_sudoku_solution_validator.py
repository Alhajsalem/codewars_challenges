# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
# ALGORITHMS DATA STRUCTURES VALIDATION

def valid_solution(board):
    count_1 = 0 
    for item in board:
        if sum(item) == 45:
            count_1 +=1
    
    count_2 = 0
    for i in range(len(board)):
        arr = []  
        for j in range(len(board)):
            arr.append(board[j][i])
        if sum(arr) == 45:
            count_2 +=1

    count_3 = 0
    for i in range(0,9,3): 
        for j in range(0,9,3):
            num = board[i][j:j+3]+ board[i+1][j:j+3] + board[i+2][j:j+3]
            if sum(num) == 45:
                count_3 +=1
    
    return True if count_1 == 9 and count_2 == 9 and count_3 == 9 else False



assert (valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8], 
                      [4, 9, 8, 2, 6, 1, 3, 7, 5], 
                      [7, 5, 6, 3, 8, 4, 2, 1, 9], 
                      [6, 4, 3, 1, 5, 8, 7, 9, 2], 
                      [5, 2, 1, 7, 9, 3, 8, 4, 6], 
                      [9, 8, 7, 4, 2, 6, 5, 3, 1], 
                      [2, 1, 4, 9, 3, 5, 6, 8, 7],
                      [3, 6, 5, 8, 1, 7, 9, 2, 4], 
                      [8, 7, 9, 6, 4, 2, 1, 3, 5]])) == False


class Ball(object):
    def __init__(self, ball_type= "regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type) 
ball2.ball_type 

class FileNameExtractor:
    def extract_file_name(f):
        return f[f.find("_")+1:f.rfind(".")]


FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")#,"FILE_NAME.EXTENSION")


def average_string(s):
    numbers = {"zero":0,"one":1,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7,
    "eight":8, "nine":9}
    str_array = s.split(" ")
    for item in str_array:
        if item not in numbers:
            return "n/a"
    result = []
    len_of_array = len(str_array)
    for i in set(s.split(" ")):
        result.append(numbers[i]*s.count(i))
    for a_key in numbers.keys():
        if (numbers[a_key] == int(sum(result)/len_of_array)):
            return a_key
print(average_string("pippi"))#, "four")