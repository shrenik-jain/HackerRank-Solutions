'''
Question : Given an integer, n, print the following values for each integer i from 1 to n:
           1.Decimal
           2.Octal
           3.Hexadecimal (capitalized)
           4.Binary
           The four values must be printed on a single line in the order specified above for each i from 1 to n. 
           Each value should be space-padded to match the width of the binary value of n.
           
Link : https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
   
    width = len(bin(number)[2:])
    
    for i in range(1 , number + 1): 
        
        octa = str((oct(i)[2:])).rjust(width, ' ')
        hexa = ((hex(i)[2:]).upper()).rjust(width, ' ')
        binary = (bin(i)[2:]).rjust(width, ' ')
        num = str(i).rjust(width, ' ')
        
        print(f'{num} {octa} {hexa} {binary}')
