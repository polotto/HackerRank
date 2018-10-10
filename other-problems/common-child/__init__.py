#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the commonChild function below.
def commonChild(s1, s2):
    # common = list(set(s1).intersection(s2))
    
    # if len(s1) > len(s2):
    #     s1, s2 = s2, s1
    
    # s1_dic = defaultdict(list) 
    # for i,e in enumerate(s1):
    #     s1_dic[e].append(i)

    # child = [0]
    # for i in s2:
    #     j = s1_dic[i]
    #     if len(j) == 0:
    #         continue
        
    #     for k in j:
    #         if k > child[-1]:
    #             print(child, k)
    #             child.append(k)
    child = [-1]
    for i in range(len(s1)):
        s_i = s1[i]
        for j in range(len(s1)):
            if s_i == s2[j] and j > child[-1]:
                child.append(j)

    print(child)
    
    return  len(child)

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input01.txt'), 'r')
    
    s1 = fptr_input.readline().rstrip()

    s2 = fptr_input.readline().rstrip()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
