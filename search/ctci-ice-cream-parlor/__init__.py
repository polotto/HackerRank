#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_s = sorted(enumerate(cost), key = lambda x: x[1])
    fil_cost = []
    j = 0
    while len(fil_cost) == 0:
        ice_a = cost_s[j]
        ice_b_cost = money - ice_a[1]
        ice_b = (len(cost), 0)
        fil_cost = list(filter(lambda x: x[1] == ice_b_cost , cost_s[j+1:]))
        for i in fil_cost:
            if i[0] < ice_b[0]:
                ice_b = i
        j += 1
    if ice_a[0] > ice_b[0]:
        ice_a, ice_b = ice_b, ice_a
    print(ice_a[0] + 1, ice_b[0] + 1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
