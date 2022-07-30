def count_sheep(n):
    result = ""
    for i in range(1,n+1):
        result += str(i)+ " sheep..."
    return result

""" def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1)) """

count_sheep(3)#, "1 sheep...2 sheep...3 sheep...")


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

zero_fuel(50, 25, 2)#, True)
zero_fuel(100, 50, 1)#, False)