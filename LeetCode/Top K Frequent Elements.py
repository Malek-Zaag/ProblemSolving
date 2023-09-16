import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())


for i in range(t):
    k=int(input())
    nums=[int(i) for i in input().split(',')]
    h={}
    for i in nums:
        if h.get(i)== None: h[i]=1
        else : h[i]+=1
    l=sorted(h.items(),key=lambda x: x[1],reverse=True)
    print([i[0] for i in l[:k]])
    