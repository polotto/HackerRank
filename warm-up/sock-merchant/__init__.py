#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = []
    visited = n*[False]
    for i in range(n):
        if visited[i]:
            continue
        else:
            visited[i] = True
        for j in range(i+1, n):
            if ar[i] == ar[j] and not visited[j]:
                pair.append([i, j])
                visited[j] = True
                break
    print(pair)
    return len(pair)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
