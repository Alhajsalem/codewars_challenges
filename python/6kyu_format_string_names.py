#https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
# FUNDAMENTALS STRINGS FORMATTING ALGORITHMS
def namelist(names):
    if len(names) == 0: return ''
    if len(names) == 1: return names[0]['name']
    list_names = [name['name']for name in names]
    last_name = list_names.pop()
    return(", ".join(list_names)+" & "+last_name)

assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'

# better solution
def namelist_1(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

assert namelist_1([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'


def add_arrays(array1, array2):
    if len(array1) != len(array2): raise Exception("something went wrong")
    return ([array1[i] + array2[i] for i in range(len(array1))])


# better solution 
from operator import add
def add_arrays(xs, ys):
    if len(xs) != len(ys):
        raise ValueError
    return list(map(add, xs, ys))


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[i]+ numbers[j]) == target and i != j:
                return [i,j]


print(two_sum([2,2,3], 4)) #  (0, 2)