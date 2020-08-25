#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_a , num_o = 0 , 0
    for i in apples:
        i = i+a
        if i>=s and i <=t:
            num_a = num_a+1 

    for i in oranges:
        i = i+b
        if i>=s and i <=t:
            num_o = num_o+1 

    print(num_a , num_o , sep='\n')

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
