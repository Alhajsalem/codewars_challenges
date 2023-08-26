def two_are_positive(a, b, c):
    #return sum(1 for x in args if x > 0) == 2
    return len(list(filter(lambda x: (x > 0), [a,b,c]))) == 2;


def eliminate_unset_bits(number):
    #return int( "0" + number.replace("0", ""), 2)
    number = number.replace("0", "")
    return int("0"+number, 2)
    
def filter_string(string):
    return int(''.join([letter for letter in string if letter.isnumeric()]))


filter_string("aa1bb2cc3dd")