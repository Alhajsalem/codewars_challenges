def sort_by_bit(arr):
    arr.sort(key=lambda x:(bin(x).count('1'), x))
    return arr
print(sort_by_bit( [3, 8, 3, 6, 5, 7, 9, 1]));