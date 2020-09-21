'''
Question : The students of District College have subscriptions to English and French newspapers. 
           Some students have subscribed only to English, some have subscribed to only French and some have 
           subscribed to both newspapers. You are given two sets of student roll numbers. One set has subscribed 
           to the English newspaper, and the other set is subscribed to the French newspaper. The same student could 
           be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Link : https://www.hackerrank.com/challenges/py-set-union/problem
'''

_ = int(input())
english = set(map(int , input().split()))
_ = int(input())
french = set(map(int , input().split()))

print(len(english.union(french)))
