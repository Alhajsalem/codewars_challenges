# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
# FUNDAMENTALS LISTS DATASTRUCTURES FILTERING
def filter_list(l):
  return [item for item in l if type(item) == int]
assert filter_list([1,2,'a','b']) == [1,2]
