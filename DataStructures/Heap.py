#Ryan Kelly
#2/11/2019
#CS260

import timeit
import random


#This is my attempt at making heap
class MakeHeap:

    # Heap list
    # Current Size of the heap
    def __init__(self):
        self.heapL = [0]
        self.CSize = 0

    # Building the heap
    def buildHeap(self,alist):
      n = len(alist) // 2
      self.CSize = len(alist)
      self.heapL = [0] + alist[:]
      while (n > 0):
          self.Down(n)
          n = n - 1

    # Finds the smallest child
    def MinC(self,n):
     if n * 2 + 1 > self.CSize:
        return n * 2
     else:
         if self.heapL[n*2] < self.heapL[n*2+1]:
              return n * 2
         else:
             return n * 2 + 1

    # deletes the min
    def delMin(self):
      r = self.heapL[1]
      self.heapL[1] = self.heapL[self.CSize]
      self.CSize = self.CSize - 1
      self.heapL.pop()
      self.Down(1)
      return r

    # Goes down the tree
    def Down(self, n):
        while (n * 2) <= self.CSize:
            mc = self.MinC(n)
            if self.heapL[n] > self.heapL[mc]:
                temp = self.heapL[n]
                self.heapL[n] = self.heapL[mc]
                self.heapL[mc] = temp
            n = mc


prob1 = []
count = []
i = 1

while i <= 10:
    testL = random.sample(range(1,50),10)
    mytime = timeit.Timer('MH.buildHeap('+str(testL)+')','from __main__ import MakeHeap; MH=MakeHeap()')
    delta = mytime.timeit(1)
    prob1.append(delta)
    count.append(i)
    i += 1

fmt = '%-8s%-20s%s'
print("-------Prob1-------")
print(fmt %('','N','Time'))
for i,(N,Time) in enumerate(zip(count,prob1)):
    print(fmt % (i, N, Time))

