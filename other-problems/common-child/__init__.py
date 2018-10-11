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


    if len(s1_common) > len(s2_common):
        s1_common, s2_common = s2_common, s1_common

    print(s1_common)
    print(s2_common)

    common_child = []
    for i in range(len(s1_common)):
        s1_i = s1_common[i]
        for j in range(len(s2_common)):
            if s1_i == s2_common[i]:
                common_child.append(s1_i)
                s2_common = s2_common[j:]
                break


    print(s1_common)
    print(s2_common)
    print(common_child)
    
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
    # child = [-1]
    # numbers = [-1]
    # i = 0
    # while i < len(s1_common):
    #     s_i = s1_common[i]
    #     remove = False
    #     for j in range(len(s2_common)):
    #         if s_i == s2_common[j]:
    #             s1_common.pop(i)
    #             s2_common.pop(j)
    #             child.append(j)
    #             numbers.append(s_i)
    #             remove = True
    #             break
    #     if not remove:
    #         i += 1

    # print(child)
    # print(numbers)
    
    return  len(common_child)

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input14.txt'), 'r')
    
    s1 = fptr_input.readline().rstrip()

    s2 = fptr_input.readline().rstrip()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
