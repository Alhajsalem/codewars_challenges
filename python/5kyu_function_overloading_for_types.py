# https://www.codewars.com/kata/6025224447c8ed001c6d8a43/train/python
# FUNDAMENTALS FUNCTIONS CONTROLFLOW BASIC LANGUAGE FEATURES METHODS OBJECT-ORIENTED PROGRAMMING
from collections import defaultdict
from functools import wraps

CACHE = defaultdict(lambda:defaultdict(lambda:None))

def overload(*type_of_input):
    def dec(func):
        overloads = CACHE[func.__qualname__]
        overloads[type_of_input] = func
        @wraps(func)
        def wrapper(*a,**kw):
            typs = tuple(type(v) for v in a+tuple(kw.values()))
            func_n    = overloads[typs] or overloads[typs[1:]]
            return func_n(*a,**kw)
        return wrapper
    return dec


# better and easier solution 
D = {}

def overload_1(*input_types):
    def outer(f):
        s = str(f).split()[1]
        D[(s, input_types)] = f
        def inner(*args, **kwargs):
            a = tuple(map(type, (*args, *kwargs.values())))
            g = D[(s, a)] if (s, a) in D else D[(s, a[1:])]
            return g(*args, **kwargs)
        return inner
    return outer


def add(n):
    def wrapper_1(m):
        return n+m
    return wrapper_1

add_one = add(1)
print(add_one(3))#, 4)