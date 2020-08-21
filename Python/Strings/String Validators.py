if __name__ == '__main__':
    str = input()
    for i in ('isalnum' , 'isalpha' , 'isdigit','islower', 'isupper'):
        print(any(eval("a." + i + "()") for a in str))
