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

# https://www.codewars.com/kata/5ebcfe1b8904f400208e3f0d/train/python

class FuncAdd:  
    data = []
    def __init__(self,func):
        self.func = func
        self.data.append(func)
        setattr(FuncAdd,'data',self.data)
        
    def __call__(self,*a,**k):
        if self.func not in self.data:
            raise NameError
        return tuple(i(*a,**k) for i in self.data if i.__name__==self.func.__name__) 
    
    @classmethod
    def delete(cls,func_name):
        cls.data = list(filter(lambda c: c.__name__!=func_name.func.__name__,cls.data))
    
    clear = classmethod(lambda cls: cls.data.clear())
        


@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

print(foo()) #--> ('Hello', 'World')


FuncAdd.delete(foo) # Delete all foo() functions only
print(foo())