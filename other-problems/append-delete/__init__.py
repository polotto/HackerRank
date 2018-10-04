#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # the special case when k > len(s)
    if k > len(s) and len(s) + len(t) > k:
        print(len(s), len(t))
        return 'No'

    # create a copy
    s_norm = s
    t_norm = t
    norm_char = '*'
    # normalize to both have the same size
    if len(s) > len(t):
        t_norm  = t_norm + (len(s) - len(t))*norm_char
    elif len(s) < len(t):
        s_norm = s_norm + (len(t) - len(s))*norm_char
    print(t_norm, s_norm)
    # generate a list to iterate throught all elements
    s_split = list(s)
    t_split = list(t)
    s_split_norm = list(s_norm)
    t_split_norm = list(t_norm)
    print(s_split_norm, t_split_norm)
    
    # iterate and stop at first difference
    for i in range(len(t_split_norm)):
        # if is different and s or t isn't a norm_char, add to the counter
        if t_split_norm[i] != s_split_norm[i] and \
        (t_split_norm[i] != norm_char or s_split_norm[i] != norm_char):
            break;
    print(s_split[i:])
    print(t_split[i:])
    # made the count how many letter need be changed after the first difference
    count = len(s_split[i:]) + len(t_split[i:]) 
    print(count)
    
    # check if pass the k
    if abs(count) > k:
        return 'No'
    else:
        return 'Yes'

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    fptr = open(os.path.join(path, './output.txt'), 'w')

    s = 'y'#'abcd'#input() # initial string

    t = 'yu'#'abcdert'#input() # desired array

    k = 2#10#int(input()) # number of changes

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')
    print(result)
    fptr.close()
