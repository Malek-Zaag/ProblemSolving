import sys
import math
from collections import Counter
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ht={}
output=""

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ht[ext.lower()]=mt

for i in range(q):
    fname=input().rsplit(".",1)
    try:
        fname_ext=fname[1].lower()
    except:
        print("UNKNOWN") 
        continue
    try: 
        if fname_ext in list(ht.keys()):
            print(ht[fname_ext])
        else :
            print("UNKNOWN")
    except:
        print("UNKNOWN")
