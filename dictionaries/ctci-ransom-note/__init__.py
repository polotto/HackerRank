#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_hash = {}
    for i in range(len(magazine)):
        if not magazine[i] in magazine_hash:
            magazine_hash[magazine[i]] = 1
        else:
            magazine_hash[magazine[i]] += 1

    ans = 0
    for string in note:
        if string in magazine_hash:
            magazine_hash[string] -= 1
            ans += 1
            if magazine_hash[string] == 0:
                del magazine_hash[string]
        else:
            break
    
    if ans == len(note):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    scr_path = os.path.dirname(__file__)
    fpr_input = open(os.path.join(scr_path, './input01.txt'), 'r')

    mn = fpr_input.readline().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = fpr_input.readline().rstrip().split()

    note = fpr_input.readline().rstrip().split()

    checkMagazine(magazine, note)
