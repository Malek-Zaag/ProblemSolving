import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    tab=input().split(",")
    s=set()
    for i in tab:
        s.add(i)
    if len(s) == len(tab):
        print(False)
    else: print(True)