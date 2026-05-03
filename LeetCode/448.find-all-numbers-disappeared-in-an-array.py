#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        n = len(nums)
        ht={}
        for i in nums:
            if i in ht: pass 
            else: ht[i]=1
        for i in range(1,n+1):
            if i not in ht:
                res.append(i)
        return res    
# @lc code=end

