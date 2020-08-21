def wrap(string, max_width):
    s="\n".join([string[i:i+max_width] for i in  range(0,len(string),max_width)])
    return s  

