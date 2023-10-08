class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        n= len(nums)
        dp= [*nums]
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1] 
    