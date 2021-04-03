# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
# ALGORITHMS ARRAYS MAP/REDUCE
def pick_peaks(arr):
    peak = None
    index = []
    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            peak = i
        elif arr[i-1] > arr[i] and peak:
            index.append(peak)
            peak = None
    return {'pos': index, 'peaks': [arr[i] for i in index]}


assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}