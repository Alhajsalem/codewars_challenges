def parse(data):
    count = 0;
    output = []   
    for it in data:
        if it == "i":
            count = count +1
        elif it == "s":
            count = count * count
        elif it == "d":
            count = count -1
        elif it == "o":
            output.append(count)
    return(output)

parse("ooo")#  ==>  [8, 64]

def parse(data):
    action = {'i': lambda v, r: v + 1,
              'd': lambda v, r: v - 1,
              's': lambda v, r: v * v,
              'o': lambda v, r: r.append(v) or v}
    v, r = 0, []
    for a in data:
        v = action[a](v, r) if a in action else v
    return r

from collections import Counter
def letter_count(s):
    return Counter(s)
print(letter_count('arithmetics')) #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
up_array([])#, [2,4,0]

def nbr_of_laps(x, y):
    for i in range(1,1000):
        for j in range(1,1000):
            if(x *i  == y*j):
                if (x > y):
                    return tuple(sorted((i,j)))
                else:
                    return (i,j)

def nbr_of_laps(x, y):
    a, b = x, y
    remain = a % b
    while remain > 0:
        a, b = b, remain
        remain = a % b

    gcd = b
    lcm = x * y / gcd

    return lcm / x, lcm / y
print(nbr_of_laps(4688, 5688))#, (1,1))

