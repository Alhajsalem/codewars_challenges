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