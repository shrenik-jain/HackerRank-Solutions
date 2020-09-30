'''
Question : In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
           There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
           Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Link : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''

from collections import defaultdict

d = defaultdict(list)
memo = []
n, m = map(int , input().split())

for i in range(n):
    d[input()].append(i+1) 

for i in range(m):
    memo = memo + [input()]  

for i in memo: 
    if i in d:
        print (" ".join(map(str,d[i])))
    else:
        print (-1)
