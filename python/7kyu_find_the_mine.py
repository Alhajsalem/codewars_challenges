def mineLocation(field):
    for index_1,ele_1 in enumerate(field):
        for index_2, ele_2 in enumerate(ele_1):
            if ele_2 == 1:
                return[index_1,index_2]

# better solution with numpy
from numpy import where, array
def mineLocation_1(field):
    x, y = where(array(field) == 1)
    return [int(x), int(y)]


mineLocation_1([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ])#, [0, 0])

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True
    
def is_twinprime(n):
    return (isPrime(n) and isPrime(n-2)) or (isPrime(n) and isPrime(n+2))
print(is_twinprime(768199))#, True

from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)

b = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600'] 
c = ['A', 'B', 'C', 'D']

(A : 0) - (B : 1290) - (C : 515) - (D : 600)
stock_list(b, c),# "(A : 200) - (B : 1140)")