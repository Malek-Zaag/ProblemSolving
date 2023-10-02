import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    a,b =input().split(",")
    res=""
    carry=0
    a=a[::-1]
    b=b[::-1]
    for i in range(max(len(a),len(b))):
        digitA=ord(a[i]) - ord("0") if i < len(a) else 0
        digitB=ord(b[i]) - ord("0") if i < len(b) else 0
        
        chr=str((digitA + digitB + carry) % 2)
        res= chr + res
        carry= (digitA + digitB + carry) //2 
    if carry:
        res = "1" + res
        
              
    return res


for _ in range(int(input())):
    solve()