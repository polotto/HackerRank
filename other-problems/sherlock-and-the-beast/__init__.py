#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    z = n
    while(z % 3 != 0): 
        z -= 5 
    if(z < 0): 
        print('-1') 
    else: 
        print(z * '5' + (n-z) * '3')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
