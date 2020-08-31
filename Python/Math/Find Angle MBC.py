# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = int(input())
b = int(input())

print(round(math.degrees(math.atan(a/b))), u'\N{DEGREE SIGN}' , sep='')
