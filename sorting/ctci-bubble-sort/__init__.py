import math
import os
import random
import re
import sys

def countSwaps(a):
    swaps = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    
    print('Array is sorted in %s swaps.' % swaps)
    print('First Element: %s' % a[0])
    print('Last Element: %s' % a[-1])

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(scr_dir, './input/input03.txt'), 'r')
    
    n = int(fp_in.readline())

    a = list(map(int, fp_in.readline().rstrip().split()))

    countSwaps(a)