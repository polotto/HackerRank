#!/bin/python3

import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    s_hash = {}
    max_len = len(s) + 1
    for i in range(max_len):
        for j in range(max_len - i):
            # sort and convert list to string
            aux = ''.join(map(str, sorted(s[j:j+i])))
            # remove empty strings
            if not aux:
                continue
            # create a hash
            elif not aux in s_hash:
                print('new hash', aux)
                s_hash[aux] = 1
            # increment if already exists
            else:
                print('already hash', aux)
                s_hash[aux] += 1
    
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
