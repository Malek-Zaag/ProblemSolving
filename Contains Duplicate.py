import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    sett=set()
    res=False
    nums=input().split(",")
    nums=[int(num) for num in nums]
    for j in nums:
        if j in sett:
            res=True
            break
        else : 
            sett.add(j)
    print(res)
