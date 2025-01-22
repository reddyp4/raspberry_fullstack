#Get parameters from command line and print them

import sys

#Example Python code
def str_operation(strn, num):
    a=num*(strn+' ')
    print(a)

#sys.argv[] are the command line arguements
#note: command line is strings
str_operation(sys.argv[1],int(sys.argv[2]))
