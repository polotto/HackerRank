#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the commonChild function below.
def commonChild(s1, s2):
    common = list(set(s1).intersection(s2))
    s1_common = [n for n in s1 if n in common]
    s2_common = [n for n in s2 if n in common]
    # s1_common = s1
    # s2_common = s2

    if len(s1_common) > len(s2_common):
        s1_common, s2_common = s2_common, s1_common

    print(s1)
    print(s2)

    common_child = []
    i = 0
    while i < len(s1_common):
        s1_i = s1_common[i]
        if s1_i in s2_common:
            j = s2_common.index(s1_i)
            s1_common.pop(i)
            s2_common.pop(j)
            common_child.append(s1_i)
        i += 1

    # k = 0
    # for i in range(len(s1_common)):
    #     s1_i = s1_common[i]
    #     for j in range(k, len(s2_common)):
    #         if s1_i == s2_common[j]:
    #             common_child.append(s1_i)
    #             k = j + 1
    #             break


    print(''.join(map(str, s1_common)))
    print(''.join(map(str, s2_common)))
    print(common_child)
    
    return  len(common_child)

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input02.txt'), 'r')
    
    s1 = fptr_input.readline().rstrip()

    s2 = fptr_input.readline().rstrip()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
