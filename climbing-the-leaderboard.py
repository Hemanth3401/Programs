#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

n = int(input())
scores = map(int,input().split())
m = int(input())
alice = map(int,input().split())

leaderboard = sorted(set(scores), reverse = True)
l = len(leaderboard)

for a in alice:
    while (l > 0) and (a >= leaderboard[l-1]):
        l -= 1
    print(l+1)