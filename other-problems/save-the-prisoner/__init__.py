#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # n prinsioners
    # m sweets
    # s start seat
    # The count does't start in the position 0
    # the % operator return a full circle turn
    # include that the same prisioner that started
    # so, need add -1 to remove the count of the prisioner that started 
    result = int(m + s) % int(n) - int(1)
    # if less then 0 other positions before last received the candy
    if result < 0:
        result = n + result
    # if == 0 , the last prisoner will receive the candy
    if result == 0:
        result = n
    return result

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr_in = open(os.path.join(scr_dir, './input05.txt'), 'r')
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')

    t = int(fptr_in.readline())

    for t_itr in range(t):
        nms = fptr_in.readline().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        output = str(result) + '\n'
        print(output)
        fptr.write(output)

    fptr.close()
