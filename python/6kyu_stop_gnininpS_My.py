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