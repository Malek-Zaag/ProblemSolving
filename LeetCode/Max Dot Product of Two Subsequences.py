
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = nums1[i] * nums2[j]
            if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
            if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]

    

for _ in range(int(input())):
    print(solve())