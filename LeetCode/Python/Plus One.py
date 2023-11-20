import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    digits = int("".join(input().split(" ")))
    digits+=1
    digits=str(digits)
    return ([int(i) for i in digits])


for _ in range(int(input())):
    print(solve())