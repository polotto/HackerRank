#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # order the space station to work with one loop (O(n) time complexity)
    c_sorted = sorted(c)
    total_distance = 0 # start in the distance 0
    j = 0 # start in the first space station
    for i in range(n): # iterate through the cities
        # if the next space station is more close then actual, go to the next space station
        # incrementing j. 
        # Has a condition to avoid index out of range and keep calculating the
        # distance related with the last space station.
        actual_distance = abs(i - c_sorted[j])
        if j < (len(c_sorted) - 1) and abs(i - c_sorted[j+1]) < actual_distance:
            # increment j
            j += 1
            # update actual distance
            actual_distance = abs(i - c_sorted[j])
        
        # if the actual distance is greater then total distance, change the total distance
        # value
        if actual_distance > total_distance:
            total_distance = actual_distance
    
    # return the result
    return total_distance

def flatlandSpaceStations_old(n, c):
    dist = 0
    for i in range(n):
        nearest = n
        for j in c:
            aux = abs(i-j)
            if aux < nearest :
                nearest = aux 
        if dist < nearest:
            dist = nearest
    return dist

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)

    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input14.txt'), 'r')

    nm =fptr_input.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, fptr_input.readline().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    end = timer()
    print(end-start)
