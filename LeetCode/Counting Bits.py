import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    n = int(input())
    tab=[]
    for i in range(n+1):
        i=str(bin(i))[2:]
        tab.append(i.count('1'))
    return tab

for _ in range(int(input())):
    print(solve())