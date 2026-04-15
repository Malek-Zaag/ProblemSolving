#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        if words[startIndex] == target:
            return 0
        curr_ind=startIndex
        n=len(words)
        curr=words[startIndex]
        counter=0
        while (curr!= target):
            curr=words[(curr_ind + 1)% n]
            counter+=1
            curr_ind=(curr_ind + 1)% n
            r=counter
        counter=0
        curr_ind=startIndex
        n=len(words)
        curr=words[startIndex]
        while (curr!= target):
            curr=words[(curr_ind -1 )% n]
            curr_ind=(curr_ind - 1)% n
            counter+=1
            l=counter        
        return min(l,r)
# @lc code=end

