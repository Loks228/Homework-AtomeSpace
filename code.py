from abc import ABC, abstractmethod

class classInit(ABC):
    def __init__(self, s = ""):
        self.r = []
        self.number = []
        self.h = []
        self.s = s
        
class TwoList(classInit):
    def RList(self):
        for x in self.s:
            self.r.append(x)
        return self.r

class ThreeFilter(classInit):
    def forenge(self):
        for i in range(len(self.r)):        
            if i + 1 < len(self.r):
                n = self.r[i+1]
                if r[i] != n:
                    self.number.append(self.r[i])
                    self.number.sort()
        for x in range(len(self.number)): 
            if x + 1 < len(self.number):
                n = self.number[x+1]
                if self.number[x] == n:
                    del self.number[x]
        return self.number

class FourNumber(classInit):
    def numsum(self):
        for n in range(len(self.number)):
            self.h.append(n)
        return sum(self.h)
            


words = TwoList(str(input("Write a set of letters and write as many as possible that do not repeat; ")))
print(words.RList())
print(ThreeFilter(words).forenge())
print(FourNumber(words).numsum())
