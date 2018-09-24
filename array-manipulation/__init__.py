#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

'''
instead of storing the actual values in the array, 
you store the difference between the current element 
and the previous element. So you add sum to a[p] showing 
that a[p] is greater than its previous element by sum. 
You subtract sum from a[q+1] to show that a[q+1] is less 
than a[q] by sum (since a[q] was the last element that was 
added to sum). By the end of all this, you have an array 
that shows the difference between every successive element. 
By adding all the positive differences, you get the value 
of the maximum element.
'''
def arrayManipulation2(n, queries):
        # Big O (N)
        res = [0]*(n+1) # we only really need one terminal row, since we're applying each pass to all rows below

        # loop through all the queries and apply the increments/decrements for each
        # Big O (M) (size of queires)
        for row in range(len(queries)):
                a = queries[row][0]
                b = queries[row][1]
                k = queries[row][2]

                res[a-1] += k # increment the starting position
                # this is where a loop would increment everything else between a & b by k
                # but instead of taking b-a steps, we take a constant 2 steps, saving huge on time
                res[b] -= k # decrement the position AFTER the ending position

        # now loop through res one time - Big O (N) (size of res)
        sm = 0 # running sum
        mx = 0 # maximum value found so far
        for i in range(len(res)):
                sm += res[i]
                if sm > mx:
                        mx = sm

        # total run time is Big O (2*N + M) >> Big O(N)
        return mx

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    
    for q in queries:
        arr[q[0]-1] += q[2]
        arr[q[1]] -= q[2]

    sum_arr = 0
    maximum = 0
    for i in arr:
        sum_arr += i
        maximum = max(sum_arr, maximum)
    return maximum

def arrayManipulationBruteForce(n, queries):
    arr = [0]*n
    maximum = 0
    
    for q in queries:
        for i in range(q[0] - 1, q[1]):
            arr[i] += q[2]
            maximum = max(maximum, arr[i])
    
    return maximum

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_in = open(os.path.join(scr_dir, './input04.txt'), 'r')

    nm = fptr_in.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, fptr_in.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    print(timer() - start)
