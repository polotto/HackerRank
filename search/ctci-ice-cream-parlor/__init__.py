#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# Complete the whatFlavors function below.
def whatFlavors2(cost, money):
    print(cost)    
    cost_s = sorted(enumerate(filter(lambda x: x < money, cost)), key = lambda x: x[1])
    print(cost_s)
    fil_cost = []
    j = 0
    while len(fil_cost) == 0:
        ice_a = cost_s[j]
        ice_b_cost = money - ice_a[1]
        ice_b = (len(cost), 0)
        fil_cost = list(filter(lambda x: x[1] == ice_b_cost , cost_s[j+1:]))
        ice_b = fil_cost[0] if fil_cost else ice_b
        j += 1

    if ice_a[0] > ice_b[0]:
        ice_a, ice_b = ice_b, ice_a
    print(ice_a[0] + 1, ice_b[0] + 1)
    
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def binarySearch(elem, a):
    left = 0
    right = len(a) - 1
    mid_i = None
    mid = None
    found = False
    while left <= right and not found:
        mid_i = (left + right)//2
        mid = a[mid_i]
        if mid[1] == elem:
            found = True
        elif elem > mid[1]:
            left = mid_i + 1
        elif elem < mid[1]:
            right = mid_i - 1
    
    return mid

def whatFlavors3(cost, money):
    cost_f = cost
    cost_enum = list(enumerate(cost))
    N = len(cost_enum)
    ice_a = None
    ice_b = None
    for i in range(N):
        ice_a = cost_enum[i]
        ice_b_price = money - ice_a[1]
        if ice_b_price in cost_f[i+1:]:
            ice_b = list(filter(lambda x: x[1] == ice_b_price, cost_enum[i+1:]))[0]
            break
    
    if ice_a[0] > ice_b[0]:
        ice_a, ice_b = ice_b, ice_a
    print(ice_a[0] + 1, ice_b[0] + 1)

def whatFlavors(cost, money):
    map = {}
    for i, v in enumerate(cost):
        ice_b = money - v
        if ice_b in map:
            print(map[ice_b], i + 1)
            break
        else:
            map[v] = i + 1

if __name__ == '__main__':
    start = timer()
    test_case = '00'
    scr_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(scr_dir, './input/input%s.txt' % test_case), 'r')
    t = int(fp_in.readline().rstrip())

    for t_itr in range(t):
        money = int(fp_in.readline().rstrip())

        n = int(fp_in.readline().rstrip())

        cost = list(map(int, fp_in.readline().rstrip().split()))

        whatFlavors(cost, money)

    print(timer()-start)