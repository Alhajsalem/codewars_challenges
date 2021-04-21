#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    result = []
    for item in sentence.split(" "):
        if len(item) >= 5:
            result.append(item[::-1])
        else:
            result.append(item)

    return " ".join(result)
    
spin_words("Hey fellow warriors")


# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    return "{} {}".format(str(max([int(i) for i in numbers.split(" ")])),str(min([int(i) for i in numbers.split(" ")])))


high_and_low("1 2 3 4 5")  # return "5 1"