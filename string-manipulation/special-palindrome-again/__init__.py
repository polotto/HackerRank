#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the substrCount function below.
def substrCount(n, s):
    s_palindrome = 0
    i = 0
    for i in range(n):
        for j in range(n - i):
            sub_s = s[j:j+i]
            if  sub_s == sub_s[::-1]:
                freq = Counter(sub_s)
                len_freq = len(freq)
                
                if len_freq == 1:
                    s_palindrome += 1
                    continue
                    
                N = len(sub_s)
                if len_freq == 2 and N % 2 != 0 and sub_s[N//2] != sub_s[0]:
                    s_palindrome += 1
    
    return s_palindrome
                    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
