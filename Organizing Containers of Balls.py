#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
q = int(input())
for a0 in range(q):
    n = int(input())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().split(' ')]
        M.append(M_t)
    rowSums = []
    colSums = []
    for i in range(n):
        rowSums.append(sum(M[i]))
    for i in range(n):
        colSum = 0
        for j in range(n):
            colSum += M[j][i]
        colSums.append(colSum)
    if sorted(rowSums) == sorted(colSums):
        print ("Possible")
    else:
        print ("Impossible")