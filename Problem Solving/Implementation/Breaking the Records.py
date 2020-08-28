#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest  , lowest = 0 , 0
    high , low = scores[0] , scores[0]
    for i in scores[1:]:
        if i>high:
            high = i
            highest+=1

        if i<low:
            low = i
            lowest+=1

    return [highest ,lowest]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
