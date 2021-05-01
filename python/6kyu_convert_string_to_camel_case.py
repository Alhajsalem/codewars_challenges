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

#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
import re
def validate_pin(pin):
    return True if re.fullmatch(r'\d{4}|\d{6}', pin) else False

assert validate_pin("1234") == True

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()


#https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class add(int): 
    def __call__(self, n):
        return add(self+n)

x = add(1)(2)


class Person(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __setattr__(self,name, value):
        if isinstance(value, str):
            self.__dict__[name] = value.upper()
        else:
            self.__dict__[name] = value*150
    def __repr__(self):
        return "Person Object with following name {} and age {}".format(self.name, self.age)

per = Person("Hans Müller",22)
