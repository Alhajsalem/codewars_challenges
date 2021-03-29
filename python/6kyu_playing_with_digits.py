#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS
def dig_pow(n, p):
    k = sum([int(item)**(p+index) for index,item in enumerate(str(n))])/n
    return k if k-int(k) == 0 else -1 
    
assert (dig_pow(46288, 3)) ==  51
assert (dig_pow(46288, 5)) ==  -1

# better solution 
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k