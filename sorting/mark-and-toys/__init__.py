import os
import math
import sys
from timeit import default_timer as timer
from collections import Counter

def bubleSort(a):
    sorted = False
    j = 1
    while not sorted:
        sorted = True
        for i in range(len(a) - j):
            if  a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                sorted = False
        j += 1

def countingSort2(a):
    count = [0] * (max(a) + 1)
    for x in a:
        count[x] += 1
    
    total = 0
    for i in range(len(count)):
        oldCount = count[i]
        count[i] = total
        total += oldCount

    output = [0] * len(a)
    for x in a:
        output[count[x]] = x
        count[x] -= 1

    return output

def countingSort(a):
    count = [0] * (max(a) + 1)
    for x in a:
        count[x] += 1
    
    total = 0
    for i in range(len(count)):
        oldCount = count[i]
        count[i] = total
        total += oldCount

    output = [0] * len(a)
    for x in a:
        output[count[x]] = x
        count[x] -= 1

    return output


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    total_price = 0
    total_toys = 0
    for toy in prices:
        if total_price + toy < k:
            total_price += toy
            total_toys += 1
        else:
            break
    
    return total_toys

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_in = open(os.path.join(scr_dir, './input/input06.txt'), 'r')

    nk = fptr_in.readline().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, fptr_in.readline().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    print(result)
    print(timer() - start)