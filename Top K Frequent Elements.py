import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())


for i in range(t):
    k=int(input())
    tab=input().split(",")
    tab=[int(k) for k in tab]
    h={}
    for j in tab:
        h[j]=h.get(j,0)+1
    print(h)
    res=dict(sorted(h.items(), key=lambda item: item[1],reverse=-1))
    res=list(res.keys()) 
    print(res[:k])