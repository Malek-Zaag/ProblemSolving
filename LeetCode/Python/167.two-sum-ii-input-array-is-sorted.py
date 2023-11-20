#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,1
        while numbers[i] + numbers[j] != target:
                if numbers[i]==numbers[j]:
                    i+=1
                    j+=1
                if j == len(numbers)  -1:
                    i+=1
                    j=i+1
                else: 
                    j+=1
        return [i+1,j+1]
# @lc code=end

