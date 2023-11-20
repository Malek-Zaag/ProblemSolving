class Solution:
    def integerBreak(self, n: int) -> int:
        dp= [1] * (n+1)
        for i in range(1,n+1):
            for j in range(1,i+1 if i!=n else i ):
                dp[i] = max(dp[i], dp[i -j ] * j)
        return dp[-1]
        