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

