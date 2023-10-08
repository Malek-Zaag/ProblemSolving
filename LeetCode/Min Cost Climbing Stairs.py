
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    cost = list(map(int, input().split()))
    if not cost:
        return 0
    dp = [0] * len(cost)
    dp[0] = cost[0]
    if len(cost) >= 2:
        dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

for _ in range(int(input())):
    print(solve())