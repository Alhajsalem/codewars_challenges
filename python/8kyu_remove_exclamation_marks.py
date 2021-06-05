def remove_exclamation_marks(s):
    return s.replace("!","")
remove_exclamation_marks("Hello World!"), "Hello World"


def pipe_fix(nums):
    return [i for i in range(min(nums),max(nums)+1)]

pipe_fix([1, 2, 3, 5, 6, 8, 9])


def validate(n):
    arr_result_1= []
    for i in range(0,len(str(n)),1):
        if i %2 == 0:
            arr_result_1.append(int(str(n)[i])*2)
        else:
            arr_result_1.append(int(str(n)[i]))

    arr_result_2 = []
    for i in arr_result_1:
        if i > 9:
            arr_result_2.append(int(str(i)[0])+ int(str(i)[1]))
        else:
            arr_result_2.append(i)
    return sum(arr_result_2) % 10 == 0
     
def validate(n):
    digits = [int(x) for x in str(n)]
    print(digits[-2::-2])
    even = [x*2 if x*2 <= 9 else x*2 - 9 for x in digits[-2::-2]]
    odd  = [x for x in digits[-1::-2]]
    return (sum(even + odd)%10) == 0


validate(1230)

i = 2
while i < 98:
    print(i)
    i += 1

    if i == 56:
        