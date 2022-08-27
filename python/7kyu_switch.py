def switcheroo(s):
    return s.replace("a","+").replace("b","*").replace("+","b").replace("*","a")

#https://www.codewars.com/kata/62ad72443809a4006998218a/train/python
# Like, Dislike, Nothing come from Preloaded
def like_or_dislike(lst):
    if len(lst) == 0: return "Nothing";
    on_off = lst[0];
    for i in range(1,len(lst)):
        if lst[i] != on_off:
            on_off = lst[i]
        else:
            on_off = "Nothing"
    return on_off
    #return "Nothing" if (lst[-1] == lst[-2]) else lst[-1]
  
#like_or_dislike(['Like', 'Dislike','Like','Like','Like'])

def sum_no_duplicates(l):
    return sum(filter(lambda no: l.count(no) == 1, l))
   
sum_no_duplicates([1, 1, 2, 2, 3,5])#, 3
#https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
def generate_shape(n):
    result = "";
    for i in range(2,n+1):
        result += "\n"+"+"*n
    return "+"*n +result
generate_shape(7)#, '+++\n+++\n+++')