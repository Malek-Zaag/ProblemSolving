import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")

import collections

def solve():
    chars = list(map(str, input().split()))
    s = ""
    count=collections.Counter(chars)
    for i in count:
        if count[i] > 1:
            s+=str(i) + str(count[i])
        else : s+= str(i)
    return len(s)

for _ in range(int(input())):
    print(solve())