#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    val , sea = 0 , 0
    for i in s:
        if i == 'U':
            sea = sea + 1
        else:
            sea = sea - 1
        
        if sea == 0 and i == 'U':
            val = val + 1
            
    return val



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
