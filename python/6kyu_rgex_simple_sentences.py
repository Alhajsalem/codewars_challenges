# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python
# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS
import re
def make_sentences(parts):
    return (re.sub('\s[,]', ",", re.sub('\s[.]', '', " ".join(parts)))+".")

assert make_sentences(['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']) == 'The Earth rotates around The Sun in 365 days, I know that.'



# better solution
make_sentences = lambda c:re.sub(r'(?<=\w) (?=\W)|[.\s]+$','',' '.join(c))+'.'

# better solution
def make_sentences(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'


from collections import Counter
def longest(a1, a2):
    print(Counter(a2)-Counter(a1))


longest("aretheyhere", "yestheyarehere")#, "aehrsty")