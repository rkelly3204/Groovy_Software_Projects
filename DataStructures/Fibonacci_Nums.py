#!/usr/bin/env python3

#Ryan Kelly
#CS260 HW3
#Problem 1 
#Recursive Fibonacci Numbers

import sys

def fib_num(n):
    
    if n <= 1:
        return n
    
    else:
        return (fib_num(n-1) + fib_num(n-2))

def main():

    fibn = int(sys.argv[1])

    if fibn <= 0:
        print ("1")

    else:
        print(fib_num(fibn))

if __name__ == "__main__":
    
    main()
 
