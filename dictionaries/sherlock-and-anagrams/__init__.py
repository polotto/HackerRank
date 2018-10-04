#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

def sherlockAndAnagrams(s):
    # variables initialization
    s_hash = {}
    max_len = len(s)

    # loop for though differents lengths of arranges: k-k, kk-kk, etc
    for length in range(1, max_len):
        # loop for the first letter of the combination: k, kk, kkk
        for i in range(max_len - length + 1):
            # sort is needed to find a anagram
            # i index value need be sorted just once
            s_i_list = sorted(s[i:i+length])
            # loop for the secound letter of the combination: k, kk, kkk
            for j in range(i + 1, max_len - length + 1):
                # sort j index value is needed to find a anagram
                s_j_list = sorted(s[j:j+length])

                # skip empty strings or keys and elements that are not igual (not anagram)
                if s_i_list != s_j_list:
                    continue

                # convert list to string for each element of the iteration
                s_i = ''.join(map(str, s_i_list))
                s_j = ''.join(map(str, s_j_list))
                
                # contatenate to form a key to the dictionary
                key = s_i + '-' + s_j
                # print(key, i, j)
                
                if not key in s_hash:
                    s_hash[key] = 1
                # increment increment the that already exists in the dict
                else:
                    s_hash[key] += 1
    
                # add the key to the dict and start the counter in 1

    # count all the occurences
    ans = 0
    for i in s_hash:
        # sum all anagram occurences
        ans += s_hash[i]
    return ans

    # count all the occurences too but few mili secounds slower
    # return sum([value for (k, value) in s_hash.items()])

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input02.txt'), 'r')

    q = int(fptr_input.readline())

    for q_itr in range(q):
        s = fptr_input.readline().rstrip()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')
        
        print(result)

    fptr.close()
    print(timer()-start)