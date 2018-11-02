#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    orders_time = []
    for i, o in enumerate(orders):
        orders_time.append([i + 1, o[0] + o[1]])
        
    orders_time = sorted(orders_time, key = lambda x: x[1])
    orders_delivery = [o[0] for o in orders_time]
    return orders_delivery

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
