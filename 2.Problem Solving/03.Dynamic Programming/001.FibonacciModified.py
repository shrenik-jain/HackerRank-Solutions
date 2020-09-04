import math
import os
import random
import re
import sys

def fibonacciModified(t1, t2, n , memo):
    if n<=2:
        return memo[n-1]

    else:
        for i in range(n-2):
            memo.append(memo[-2] + memo[-1]**2)

    return memo[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    memo = [t1,t2]

    result = fibonacciModified(t1, t2, n, memo)

    fptr.write(str(result) + '\n')

    fptr.close()
