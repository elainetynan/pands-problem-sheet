# es.py
#
# Reads in a text file and outputs the number of e's it contains
#
# Author: Elaine Tynan

import sys
import os


# call program from command line like this: python es.py moby-dick.txt

def countEs(text):
    count = 0
    for letter in text:
        if letter == "e":
            count +=1
    return count

def readFile():
    if os.path.exists(filename):
        with open(filename, "rt") as f:
            text = f.read()
        return countEs(text)
    else:
        return -1

filename = sys.argv[1]
print("The number of Es in the file is:",readFile())