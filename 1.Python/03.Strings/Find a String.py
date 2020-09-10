def count_substring(string, sub_string):
    n=0
    for i in range(0,len(string)):
        if string[i:len(sub_string)+i]==sub_string:
            n+=1          
    return n
