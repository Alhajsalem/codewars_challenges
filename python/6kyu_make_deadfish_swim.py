def parse(data):
    count = 0;
    output = []   
    for it in data:
        if it == "i":
            count = count +1
        elif it == "s":
            count = count * count
        elif it == "d":
            count = count -1
        elif it == "o":
            output.append(count)
    return(output)

parse("ooo")#  ==>  [8, 64]

def parse(data):
    action = {'i': lambda v, r: v + 1,
              'd': lambda v, r: v - 1,
              's': lambda v, r: v * v,
              'o': lambda v, r: r.append(v) or v}
    v, r = 0, []
    for a in data:
        v = action[a](v, r) if a in action else v
    return r