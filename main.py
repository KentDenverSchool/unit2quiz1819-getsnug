class HashTable:
    def __init__(self, capacity):
        self.m = capacity
        self.dict=[None]*10000
        self.size = 0
    def resize(self, newM):
        self.m = newM
        newDict = [None]*newM;
        for elem in self.dict:
            if elem is not None:
                newDict[self.hashCode(elem[0])] = elem
                print(elem)
                print(newDict[self.hashCode(elem[0])])
        dict = newDict

    def hashCode(self,key):
        sum=0;
        for i in range(len(key)):
            sum+=ord(key[i])*pow(2,i)
        return sum%self.m
    def put(self,key,value):
        self.size+=1
        #Checks to see if there are 80 percent of m elements in arra
        if(self.size>=self.m*.8):
            resize(self.m*2)
        h=self.hashCode(key)
        print(h)
        print(key, value)
        if(self.dict[h]==None):
            self.dict[h]=[key, value]
        else:
            print("conflict!")
            self.dict[h] = [self.dict[h], [key, value]]
            print(self.dict[h])
    def get(self,key):
        if(self.dict[self.hashCode(key)] is not None):
            for elem in self.dict[self.hashCode(key)]:
                if(elem is not None):
                    if(elem[0]==key):
                        return elem
        else:
            return None
h=HashTable(20)
h.put("a","a")
h.put("b","b")
h.put("c","c")
h.put("hello", ";")
h.put("d","d")
h.put("x", "hello")

h.put("y", "hello")
print(h.get("hello"))
print(h.get("a"))
#D and Y have a conflict, which is resolved and tested below
print(h.get("d"))
print(h.get("y"))
#Hello and b have a conflict, tested below
print(h.get("hello"))
print(h.get("b"))
h.resize(23) #tests resize function, resize currently is having issues which I need to resolve
print("array resized to 23")
print(h.get("hello"))
print(h.get("a"))
print(h.get("d"))
print(h.get("x"))
print(h.get("hello"))
print(h.get("b"))

import random,math

