#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s_list = list(s)
    total = [None]
    i, j = 0, 0
    while i < len(s_list):
        temp = s_list[i]
        if temp != total[j]:
            total.append(temp)
            del s_list[i]
            j += 1
            i -= 1
        i += 1
            
    return len(s_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
