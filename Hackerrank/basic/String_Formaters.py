'''
String Formatting is the process of representing the values of certain limit ,
printing in decimal, octal, hexadecimal and binary format
Used Functions -
hex, oct, bin in built functions and rjust() function to space pad the width between values
'''

def print_formatted(number):
    width = len("{0:b}".format(number))         # finding width using number variable in binary format
    for i in range(1,number+1):
        result = "{0} {1} {2} {3}".format(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].rjust(width).upper(), bin(i)[2:].rjust(width))
        print(result)
print_formatted(196)