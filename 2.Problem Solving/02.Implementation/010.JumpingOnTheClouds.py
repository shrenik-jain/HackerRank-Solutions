import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    length = len(c)
    steps , i = 0 , 0
    while i<length-1:
        if i < length-2 and c[i+2] == 0: 
            steps = steps + 1
            i = i + 2
        else:
            steps = steps + 1
            i=i+1 

    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
