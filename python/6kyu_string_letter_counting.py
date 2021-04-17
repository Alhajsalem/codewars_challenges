# https://www.codewars.com/kata/59e19a747905df23cb000024/train/python

def string_letter_count(s):
    x = sorted(s.lower())
    result = []
    for letter in x:
        if letter.isalpha() and letter not in result:
            result.append(str(x.count(letter)))
            result.append(letter)

    return ("".join(result))
string_letter_count("The quick brown fox jumps over the lazy dog.")