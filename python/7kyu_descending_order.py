# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
def descending_order(num):
    return int("".join(sorted(str(num),reverse=True)))


assert (descending_order(123456789) == 987654321)

def cakes(recipe, available):
    array_result =[]
    for gradient in recipe.keys():
        if gradient not in available:
            return 0
        array_result.append(int(available[gradient]/recipe[gradient]))
    return min(array_result)

# must return 2
cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
# must return 0
#cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)