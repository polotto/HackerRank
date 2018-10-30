#!/bin/python3

import os
import sys

class Tree:
    def __init__(self, data, left = -1, right = -1):
        self.data = data
        self.left = left
        self.right = right

def swapNodes(indexes, queries):
    tree = Tree(1)
    parent = tree
    for i, value_i in enumerate(indexes):
        remain = i % 3
        if remain == 0:
            parent.left = Tree(value_i[0])
            parent.right = Tree(value_i[1])
        elif remain == 1:
            parent.left.left = Tree(value_i[0])
            parent.left.right = Tree(value_i[1])
        else:
            parent.right.left = Tree(value_i[0])
            parent.right.right = Tree(value_i[1])

    return [[0], [0]]

if __name__ == '__main__':
    test_case = '00'
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fp_in = open(os.path.join(scr_dir, './input/input%s.txt' % test_case), 'r')

    n = int(fp_in.readline())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, fp_in.readline().rstrip().split())))

    queries_count = int(fp_in.readline())

    queries = []

    for _ in range(queries_count):
        queries_item = int(fp_in.readline())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

    print(result)