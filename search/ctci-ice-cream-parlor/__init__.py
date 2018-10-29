#!/bin/python3

import math
import os
import random
import re
import sys

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

def whatFlavors(cost, money):
    cost_s = sorted(enumerate(filter(lambda x: x < money, cost)), key = lambda x: x[1])
    N = len(cost_s)
    ice_a = None
    ice_b = None
    for i in range(N):
        ice_a = cost_s[i]
        found = False
        for j in range(i+1, N):
            ice_b = cost_s[j]
            total = ice_a[1] + ice_b[1]
            if money == total:
                found = True
                break
            elif total > money:
                break
        
        if found:
            break
    
    if ice_a[0] > ice_b[0]:
        ice_a, ice_b = ice_b, ice_a
    print(ice_a[0] + 1, ice_b[0] + 1)

if __name__ == '__main__':
    test_case = '00'
    scr_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(scr_dir, './input/input%s.txt' % test_case), 'r')
    t = int(fp_in.readline().rstrip())

    for t_itr in range(t):
        money = int(fp_in.readline().rstrip())

        n = int(fp_in.readline().rstrip())

        cost = list(map(int, fp_in.readline().rstrip().split()))

        whatFlavors(cost, money)
