def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        octa = str((oct(i)[2:])).rjust(width, ' ')
        hexa = ((hex(i)[2:]).upper()).rjust(width, ' ')
        binary = (bin(i)[2:]).rjust(width, ' ')
        num = str(i).rjust(width, ' ')
        print(f'{num} {octa} {hexa} {binary}')
