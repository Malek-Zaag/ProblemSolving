import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    a,b =input().split(",")
    res=""
    min_l=min(len(a),len(b))
    lock=0
    for i in range(min_l-1,0):
        if  a[i] =="1" and b[i]=="0" and lock==0:
            res= "1"+res
        elif a[i] =="1" and b[i]=="0" and lock==0 :
            res= "0"+res
        elif a[i] =="1" and b[i]=="1" and lock==0 :
            res= "0"+res
            lock=1
        if  a[i] =="1" and b[i]=="0" and lock==0:
            res= "1"+res
        elif a[i] =="1" and b[i]=="0" and lock==0 :
            res= "0"+res
            
    print(res)


for _ in range(int(input())):
    solve()