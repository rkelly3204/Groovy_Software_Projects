#!/usr/bin/env python3

#Ryan Kelly
#CS260 HW
#Fibonacci Number
#Problem 2

import sys

#Had to reset the recursion limit for this program to work correctly
sys.setrecursionlimit(2000)  


def memo(fn):
    memoList = {}

    def memo_add(i):

        if i not in memoList:
           memoList[i] = fn(i)

        return memoList[i]

    return memo_add

@memo
def fib_num(n):

    if n == 0:
        return 1
    
    elif n == 1:
        return 1

    else:
        return fib_num(n-1) + fib_num(n-2)

def main():

    fibn = int(sys.argv[1])

    print(fib_num(fibn))
    
if __name__ =="__main__":
    main()
