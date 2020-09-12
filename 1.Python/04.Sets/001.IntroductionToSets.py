'''
Question : Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the 
           average of all the plants with distinct heights in her greenhouse.
           Formula used: Average = Sum of Distinct Heights / Total Number of Distinct Heights
                                   
Link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''

def average(array):
    s = set(array)
    return sum(s)/len(s)
