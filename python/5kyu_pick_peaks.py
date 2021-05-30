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

    def  __getattr__(self,name_of_function):
        return FuncAdd(name_of_function.__name__)
        
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

foo() 

FuncAdd.delete(foo) # Delete all foo() functions only
#foo() # Should raise NameError


class A:
    def __init__(self):
        print ("init")
     
    def __call__(self):
         print ("call")

x = A()
x()


class Count:
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax 
        #self.mycurrent1 = 1000   

    def __getattr__(self, item):
        print("eee{}".format(item))
        self.__dict__[item]=0
        return 0

    def __getattribute__(self, item):
        print(item)
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item) 

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.cur)


import json
def jsonattr(filepath):
    f = open(filepath, "r")
    data = json.loads(f.read())
    f.close()

    def wrapper_fn(cls):
        setattr(cls,'foo',data['foo'])
        setattr(cls,'an_int',data['an_int'])  
        setattr(cls,'this_kata_is_awesome',data['this_kata_is_awesome'])
        return cls
    return wrapper_fn 


@jsonattr("/Users/Yousef/IdeaProjects/codewars/python/myClass.json")
class MyClass:
    pass
