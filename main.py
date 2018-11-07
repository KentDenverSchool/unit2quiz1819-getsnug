class HashTable:
    def __init__(self, capacity):
        self.m = capacity
        self.dict=[None]*self.m
    def resize(self, newM):
        self.m = newM
        newDict = [None]*newM;
        for elem in self.dict:
            if elem is not None:
                newDict[self.hashCode(elem[0])] = elem
        dict = newDict

    def hashCode(self,key):
        sum=0;
        for i in range(len(key)):
            sum+=ord(key[i])*pow(2,i)
        return sum%self.m
    def put(self,key,value):
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
        for elem in self.dict[self.hashCode(key):
            if(self.dict[self.hashCode(key)]):

h=HashTable(7)
h.put("a","a")
h.put("b","b")
h.put("c","c")
h.put("hello", ";")
h.put("d","d")
h.put("x", "hello")

h.put("y", "hello")
print(h.get("hello"))
print(h.get("a"))
print(h.get("eeee"))
print(h.get("d"))
h.resize(11)

import random,math

