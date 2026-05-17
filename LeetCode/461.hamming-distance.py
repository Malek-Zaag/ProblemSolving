#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        def helper(n):
            rep=""
            while n > 0:
                rep+=str(n % 2)
                n //=2
            return rep
        print(helper(x)[::-1])
        print(helper(y)[::-1])
        rep_x=helper(x)[::-1]
        rep_y=helper(y)[::-1]
        counter=0
        if len(rep_x) > len(rep_y):
            rep_y="0"* (len(rep_x)-len(rep_y)) + rep_y
        else:
            rep_x="0"* (len(rep_y)-len(rep_x)) + rep_x
        for i,j in zip(rep_x,rep_y):
            if i != j: counter+=1
        
        return counter     
        
# @lc code=end

