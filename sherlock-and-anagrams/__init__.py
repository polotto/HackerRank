#!/bin/python3

import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    s_hash = {}
    max_len = len(s)
    for c in range(1, max_len - 1):
        for i in range(max_len):
            for j in range(i, max_len-i):
                # sort and convert list to string
                s_i = ''.join(map(str, sorted(s[i:c])))
                s_j = ''.join(map(str, sorted(s[j:c])))
                key = s_i + s_j
                # remove empty strings
                # if not s_i or not s_j:
                #    continue
                # create a hash
                if not key in s_hash:
                    s_hash[key] = 1
                # increment if already exists
                else:
                    s_hash[key] += 1
    
    print(s_hash)
    ans = 0
    for i in s_hash:
        # case is greater then 1, anagram occurs more then one time
        if s_hash[i] > 1:
            ans += s_hash[i]

    return ans

if __name__ == '__main__':
    print(sys.version_info)

    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input01.txt'), 'r')

    q = int(fptr_input.readline())

    for q_itr in range(q):
        s = fptr_input.readline().rstrip()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')
        
        print(result)

    fptr.close()
