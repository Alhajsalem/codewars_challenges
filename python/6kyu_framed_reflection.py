# def mirror(text):
#    blabla = (max([len(x) for x in text.split(" ")])) +1
#    str_re = (max([len(x) for x in text.split(" ")])+4)*"*" + "\n*" 
#    result = [x[::-1] for x in text.split(" ")]
   
#    for re in result:
#        print(len(re))
#        str_re+=" "+str(re)+ " "* (blabla - len(re))     +"*\n*"
#    str_re+=str((max([len(x) for x in text.split(" ")])+3)*"*"  ) 
#    return str_re

def mirror(text):
    words = [w[::-1] for w in text.split()]
    max_len = max(map(len, words))
    border = ['*' * (max_len + 4)]
    words = ['* {} *'.format(w.ljust(max_len)) for w in words]
    return '\n'.join(border + words + border)



mirror("Codewars")#, "*********\n* olleH *\n* dlroW *\n*********");
                            