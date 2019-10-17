#!/usr/bin/env python3

#Ryan Kelly
#1/28/2019
#HW CS260
#Problem 3

import timeit
import prob1
import prob2
import sys
import csv

sys.setrecursionlimit(1500)

prob1 = [] # Times for prob1
count1 = []# The N values of prob1
i = 0 #Starting N value for prob1

#--------------------------------------
prob2 = []# Times for prob2
count2 = []# The N values
k = 450 #Starting N value for prob2

#--------------------------------------

# Prob1 implementation
while i <= 40:

    mytime1 =timeit.Timer('fib_num('+str(i)+')', 'from prob1 import fib_num')
    delta1 = mytime1.timeit(1)
    prob1.append(delta1)
    count1.append(i)
    i += 5 #Increment N by 5

while k <= 950:

    mytime2 = timeit.Timer('fib_num('+str(k)+')','from prob2 import fib_num')
    delta2 = mytime2.timeit(1)
    prob2.append(delta2)
    count2.append(k)
    k += 50 #increment N by 50


fmt = '%-8s%-20s%s'

#Table for Prob1
print("--------- Prob1 ----------")
print(fmt % ('','N', 'Time'))
for i,(N,Time) in enumerate(zip(count1,prob1)):
    print(fmt % (i,N,Time))


print("\n")

#Table for Prob2
print("--------- Prob2 ----------")
print(fmt % ('','N', 'Time'))
for o,(N1,Time1) in enumerate(zip(count2,prob2)):
    print(fmt % (o,N1,Time1))
