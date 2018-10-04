#!/bin/python3

from timeit import default_timer as timer

import math
import os
import random
import re
import sys

# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def insertionSort(alist, ans):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         ans[0] += 1
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = [0]

    # check if the queue is too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            print('Too chaotic')
            return
    
    insertionSort(q, ans)
    print(ans[0])

# first ans worst solution
def minimumBribes2(q):
    r = list(range(1, len(q) + 1))
    ans = 0
    i = 0
    for i in range(len(q)-1):
        qi = q[i]
        if r[i] != qi:
            #print(r)
            ir = r.index(qi, qi - 1, qi + 6)
            #print(ir, q[i] - 1)
            r.insert(i, r.pop(ir))
            bribes = abs(ir - i)
            if bribes > 2:
                print('Too chaotic')
                return
            ans = ans + bribes
    print(ans)

if __name__ == '__main__':
    start = timer()
    dir_scr = os.path.dirname(__file__)
    input_tests = open(os.path.join(dir_scr, './input08.txt'), 'r')
    
    t = int(input_tests.readline())

    for _ in range(t):
        n = int(input_tests.readline())

        q = list(map(int, input_tests.readline().rstrip().split()))

        minimumBribes(q)
    
    end = timer()
    print(end-start)