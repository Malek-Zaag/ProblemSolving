import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    gain = list(map(int, input().split()))
    maxi=0
    curr_sum=0
    for i  in gain:
        curr_sum+=i
        maxi=max(maxi, curr_sum)
    return maxi


for _ in range(int(input())):
    print(solve())