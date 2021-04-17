# https://www.codewars.com/kata/59e19a747905df23cb000024/train/python

def string_letter_count(s):
    x = sorted(s.lower())
    result = []
    for letter in x:
        if letter.isalpha() and letter not in result:
            result.append(str(x.count(letter)))
            result.append(letter)

    return ("".join(result))
string_letter_count("The quick brown fox jumps over the lazy dog.")

# https://www.codewars.com/kata/5af5c18786d075cd5e00008b/train/python

DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1,5)

class Table:

    def __init__(self, data):
        self.data = data
        self.x = len(data)
        self.y = len(data[0])

    def walk(self, dir0, dir1):
        if dir0 == DIRECTION_RIGHT and dir1 == DIRECTION_DOWN:
            arr = []
            for i in range(self.x):
                for j in range(self.y):
                    arr.append(self.data[i][j])
            return arr         
        elif dir0 == DIRECTION_DOWN and dir1 == DIRECTION_RIGHT:
            arr = []
            for j in range(self.y):
                for i in range(self.x):
                    arr.append(self.data[i][j])
            return arr 
           
        elif dir0 == DIRECTION_LEFT and dir1 == DIRECTION_DOWN:
            arr = []
            for i in range(self.x):
                for j in range(self.y-1,-1,-1):
                    print(i,j)
                    arr.append(self.data[i][j])
            return arr 
           
        elif dir0 == DIRECTION_DOWN and dir1 == DIRECTION_LEFT:
            arr = []
            for j in range(self.y-1,-1,-1):
                for i in range(self.x):
                    arr.append(self.data[i][j])
            return arr 
           
        elif dir0 == DIRECTION_RIGHT and dir1 == DIRECTION_UP:
            arr = []
            for i in range(self.x-1,-1,-1):
                for j in range(self.y):
                    arr.append(self.data[i][j])
            return arr 
           
        elif dir0 == DIRECTION_UP and dir1 == DIRECTION_RIGHT:
            arr = []
            for j in range(self.y):
                for i in range(self.x-1,-1,-1):
                    arr.append(self.data[i][j])
            return arr            
        elif dir0 == DIRECTION_LEFT and dir1 == DIRECTION_UP:
            arr = []
            for i in range(self.x-1,-1,-1):
                for j in range(self.y-1,-1,-1):
                    arr.append(self.data[i][j])
            return arr 
                
        elif dir0 == DIRECTION_UP and dir1 == DIRECTION_LEFT:
            arr = []
            for j in range(self.y-1,-1,-1):
                for i in range(self.x-1,-1,-1):
                    arr.append(self.data[i][j])
            return arr 
            

t = Table([[ 5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14], 
            [15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24]])

print(t.walk(DIRECTION_DOWN, DIRECTION_LEFT))
