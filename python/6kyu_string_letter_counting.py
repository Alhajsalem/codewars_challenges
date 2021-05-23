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

t.walk(DIRECTION_DOWN, DIRECTION_LEFT)

# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    result = sum([int(x)for x in str(n)])
    if result < 10:
        return result
    else:
        return digital_root(result)

def digital_root(n):
    while n >= 10:
        n = sum(divmod(n, 10))
    return n

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
def snail(array):
    results = []
    while len(array) > 0:
        results = results + array[0]
        del array[0]
        if len(array) > 0:
            for i in array:
                results = results + [i[-1]]
                del i[-1]
            if array[-1]:
                results = results+ array[-1][::-1]
                del array[-1]
            for i in (array):
                results = results + [i[0]]
                del i[0]
    return results

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)

# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return False if len(string) != 0 else True

# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    return sum([int(i) for i in "{0:b}".format(n)])
count_bits(10)#, 2

# better solution 
def countBits(n):
    return bin(n).count("1")


# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
import re
def domain_name(url):
    pattern = re.compile(r"https://www.|http://|https://|www.")
    matches = pattern.finditer(url)
    url_start = ""
    for match in matches:
        url_start = url[match.span()[1]:]
    if url_start != "":  
        return(url_start[0:url_start.find(".")])
    else:
        return (url[0:url.find(".")])
domain_name("icann.org")

# better solution 

import re
def domain_name_1(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


def domain_name_2(url):
    pattern =  re.compile('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.')
    subbed_urls = pattern.search(url).group("name")
    return subbed_urls

# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):
    pattern =  re.compile(r'[:;]{1}[-~]?[)D]{1}')
    count=0
    for item in arr:
        if pattern.match(item) != None:
            count +=1
    return count

# better solution

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))



def word_mesh(words):
    for index,word in enumerate(words):
        for i in range(len(word),0,-1):
            print(word[i])



word_mesh(["allow", "lowering"])