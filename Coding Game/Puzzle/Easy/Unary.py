import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binmsg="".join(format(ord(x), 'b').zfill(7) for x in message)

res=""
for index, n in enumerate(binmsg):
    if index >=1 and binmsg[index]==binmsg[index-1]:
        res+="0"
    else:
        if n=="1":
            res+=" 0 0"
        elif n == "0": 
            res+=" 00 0" 
res=res[1:]
print(res)
