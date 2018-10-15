#!/bin/python3

import math
import os
import random
import re
import sys
from functools import cmp_to_key

def countInversionsBubbleSort(arr):
    swaps = 0
    N = len(arr)
    sorted_arr = False
    last_elem = 1
    while(not sorted_arr):
        sorted_arr = True
        for i in range(N - last_elem):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
                sorted_arr = False
        last_elem += 1
    
    return swaps

swaps = [0]
def comparator(a, b):
    if a > b:
        swaps[0] += 1
        return 1
    elif a < b:
        swaps[0] += 1
        return -1
    else:
        return 0

def countInversionsPythonSorted(arr):
    global swaps
    swaps = [0]
    arr_s = sorted(arr, key=cmp_to_key(comparator))
    print(arr_s)
    return swaps[0] - 1

def countInversions(arr):
    swaps = [0]
    mergeSort(arr, swaps)
    return swaps[0]

# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(arr, swaps):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf, swaps)
        mergeSort(righthalf, swaps)
        mergeHalves(arr, lefthalf, righthalf, swaps)

def mergeHalves(arr, lefthalf, righthalf, swaps):
    i, j, k = 0, 0, 0
    n_lefthalf = len(lefthalf)
    n_righthalf = len(righthalf)
    while i < n_lefthalf and j < n_righthalf:
        if lefthalf[i] <= righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            swaps[0] += (n_lefthalf - i)
            j += 1
        k += 1

    while i < n_lefthalf:
        arr[k] = lefthalf[i]
        i += 1
        k += 1
    
    while j < n_righthalf:
        arr[k] = righthalf[j]
        j += 1
        k += 1

if __name__ == '__main__':
    scr_path = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_path, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_path,'./input/input04.txt'), 'r')

    t = int(fptr_input.readline().rstrip())

    for t_itr in range(t):
        n = int(fptr_input.readline().rstrip())

        arr = list(map(int, fptr_input.readline().rstrip().split()))

        result = countInversions(arr)
        # print(arr)
        # print(result)
        fptr.write(str(result) + '\n')

    fptr.close()