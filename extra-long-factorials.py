#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    mul=1
    while(n!=0):
        mul*=n
        n-=1
    print(mul)

if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)