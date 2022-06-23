def number_of_pairs(gloves):
   result = []; 
   for glove in set(gloves):
       result.append(int(gloves.count(glove)/2))
    return sum(result)

number_of_pairs(["red","green","blue","blue","red","green","red","red","red"])