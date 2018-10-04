#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer
from random import randint

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # initialize the dictionaries
    r2 = {}
    r3 = {}
    count = 0

    # loop throgh the arr itens
    for k in arr:
        # if k in r3 indicates the triplet already completed,
        # the count need be incremented
        if k in r3:
            count += r3[k]
        
        # if k in r2, it is the secound number of the triplet,
        # your successor (third element k*r) need be added or incremented in the r3 dict
        # because is a potencial triplet 
        if k in r2:
            if k*r in r3:
                r3[k*r] += r2[k]
            else:
                r3[k*r] = r2[k]

        # else, k is the first element of the triplet, so,
        # your seccessor (secound element k*r) need be added or incremented in the r2 dict
        # because is a potencial triplet
        if k*r in r2:
            r2[k*r] += 1
        else:
            r2[k*r] = 1
    
    return count

def countTripletsBruteForce(arr, r):
    triplets = {}
    i = 0
    for j in range(len(arr)):
        for k in range(j+1,  len(arr)):
            if arr[k] == r * arr[j]:
                for l in range(k+1, len(arr)):
                    if arr[l] == r * arr[k]:
                        triplets[i] = [j,k,l]
                        i += 1
    print(triplets)
    return len(triplets)

if __name__ == '__main__':
    start = timer()

    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input00.txt'), 'r')

    nr = fptr_input.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, fptr_input.readline().rstrip().split()))

    ans = countTriplets(arr, r)
    
    print(ans)
    
    fptr.write(str(ans) + '\n')

    fptr.close()

    print(timer() - start)


def inputGen():
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './input/input03.txt'), 'w')
    n = 100000
    r = 1
    fptr.write('%s %s\n' %(n, r))
    # aux = 1
    for i in range(0, n):
        elem = 1237
        # if randint(0,9) < 5:
        #     elem = randint(5, 5000)
        # else:
        #     aux = aux*r
        #     elem = aux
        fptr.write('%s ' % elem)

    fptr.close()