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
    triplets = {}
    
    for i in range(len(arr)):
        arr_i = arr[i]
        
        arr_i_r_r = arr_i / (r * r)
        if arr_i_r_r in triplets:
            print('rr ',arr_i, arr_i_r_r)
            triplets[arr_i_r_r] += 1
            continue
        
        arr_i_r = arr_i / r
        if arr_i_r in triplets:
            print('r ', arr_i, arr_i_r)
            triplets[arr_i_r] += 1
            continue
        
        if (arr_i == r or arr_i == 1) and (not arr_i in triplets):
            print('a0 ', arr_i)
            triplets[arr_i] = 1
            continue
            
    print(triplets)
    return sum([v for (k,v) in triplets.items()])

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
    fptr_input = open(os.path.join(scr_dir, './input/input01.txt'), 'r')

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