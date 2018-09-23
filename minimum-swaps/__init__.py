#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# source: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)

    # Create two arrays and use 
    # as pairs where first array 
    # is element and second array
    # is position of first element
    arrpos = list(enumerate(arr))

    # Sort the array by array element 
    # values to get right position of 
    # every element as the elements 
    # of second array.
    arrpos.sort(key = lambda it: it[1])

    # To keep track of visited elements. 
    # Initialize all elements as not 
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):
        # already swapped or 
        # already present at 
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue
        
        # find number of nodes 
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
        
        # update answer by adding
        # current cycle
        ans += (cycle_size - 1)
    
    # return answer
    return ans

def minimumSwapsFirstVersion(arr):
    #print(arr)
    swaps = 0
    i_pivot = 0
    for i_pivot in range(len(arr)):
        # reset vars to find the minimum
        i_swap = 0
        elem = 10**5
        # iterate to find the minimum element of arr from the actual positon
        # and save the element and the postion
        for i_test in range(i_pivot, len(arr)):
            if arr[i_test] < elem:
                elem = arr[i_test]
                i_swap = i_test
        
        # if the minimum valur isn't the actual pivot, swap values 
        if i_swap != i_pivot:
            a = arr[i_pivot]
            arr[i_pivot] = arr[i_swap]
            arr[i_swap] = a
            swaps += 1

    return swaps

if __name__ == '__main__':
    start = timer()
    dir_scr = os.path.dirname(__file__)
    fptr = open(os.path.join(dir_scr, './output.txt'), 'w')
    input_test = open(os.path.join(dir_scr, './input00.txt'), 'r')
    n = int(input_test.readline())

    arr = list(map(int, input_test.readline().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
    
    print(res)
    end = timer()
    print(end-start)