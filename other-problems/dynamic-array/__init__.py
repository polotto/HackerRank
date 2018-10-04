#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqs = []
    answers = [0]
    for i in range(n):
        seqs.append([])
    for query in queries:
        x = query[1]
        y = query[2]
        lastAnswer = answers[len(answers)-1]
        sequence = (x^lastAnswer)%n
        print(sequence, y)
        if query[0] == 1:
            seqs[sequence].append(y)
        elif query[0] == 2:
            size = len(seqs[sequence])
            newAnswer = seqs[sequence][y%size]
            print(newAnswer)
            if newAnswer != 0:
                answers.append(newAnswer)
    print(answers)
    # the 0 doesn't belong to the solution
    return answers[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
