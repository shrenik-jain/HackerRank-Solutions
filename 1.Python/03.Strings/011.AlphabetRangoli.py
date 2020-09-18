'''
Question : You are given an integer, N. 
           Your task is to print an alphabet rangoli of size N.
           size 3
           ----c----
           --c-b-c--
           c-b-a-b-c
           --c-b-c--
           ----c----
           
Link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

import string

def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    
    for i in list(range(size))[::-1] + list(range(1 , size)):
        print('-'.join(alpha[size-1 : i : -1] + alpha[i : size]).center(width , '-'))
