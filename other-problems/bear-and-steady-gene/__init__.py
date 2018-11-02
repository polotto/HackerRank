#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def balanced(n, dic):
    bal = True
    for k, v in dic.items():
        if v > n:
            bal = False
            break
    return bal

# Complete the steadyGene function below.
def steadyGene(gene):
    N = len(gene)
    g_n = N/4
    gene_freq = Counter(gene)
    
    min_ans = 10**9
    right = left = 0
    while right < N and left < N:
        if not balanced(g_n, gene_freq):
            gene_freq[gene[right]] -= 1
            right += 1
        else:
            min_ans = min(min_ans,  right - left)
            gene_freq[gene[left]] += 1
            left += 1
    
    return min_ans
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
