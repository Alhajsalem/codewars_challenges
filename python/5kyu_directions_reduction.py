# my solution 
directions = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
def dirReduc(arr):
    i = 0
    while i < len(arr)-1:
        current_item = arr[i]
        if arr[i+1] == directions[current_item]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i+=1
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
assert dirReduc(a) == ["WEST"]


# clever solution Python Recursion
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3





