# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
# REGULAR EXPRESSIONS
import re
def to_camel_case(text):
    arr = (re.sub(r'[-_]',"_",text)).split("_")
    return "".join(([arr[i].capitalize() if i >0 else arr[i] for i in range(len(arr))]))

assert to_camel_case('') == ''
assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
assert to_camel_case("The-Stealth-Warrior") =="TheStealthWarrior"
assert to_camel_case("A-B-C") == "ABC"

# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    arr_res = [seq.count(item)for item in seq]
    for item in arr_res:
        if item % 2 != 0:
            return(seq[arr_res.index(item)])
            


assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
