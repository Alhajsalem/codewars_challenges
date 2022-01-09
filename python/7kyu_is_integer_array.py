def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)

is_int_array([1, 2, None])

def pair_zeros(arr):
    lst = []
    flag = False
    for i in arr:
        if i == 0:
            if not flag:
                lst.append(i)
            flag = not flag
        else:
            lst.append(i)
    return lst


pair_zeros([1,0,1,0,2,0,0,3,0])#,[1,0,1,2,0,3,0]

def sum_digits(number):
    return sum([int(i) for i in str(abs(number))])


print(sum_digits(-32))#, 5

def incrementer(nums):
   print([ int(str((i+1+j))[-1:])  for i, j in enumerate(nums)])

incrementer([4, 6, 7, 1, 3])#, [5, 8, 0, 5, 8])

def duplicate_elements(m, n):
    for i in m:
        if i in n:
            return True
    return False

def next_smaller(n):
    countdown = n-1
    while countdown > 9:
        if "".join(sorted(str(countdown))) == "".join(sorted(str(n))):
            return countdown
        countdown = countdown - 1
    return -1
    
print(next_smaller(123456789))#, 790

def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    last_layer = pyramid[-1]
    add_layer = []
    
    for i in range(1, len(last_layer)):
        add_layer.append(max(last_layer[i], last_layer[i-1]))

    pyramid[-2] = [a+b for a, b in zip(pyramid[-2], add_layer)]
    print(pyramid[-2])
    return longest_slide_down(pyramid[:-1])

print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))#, 23