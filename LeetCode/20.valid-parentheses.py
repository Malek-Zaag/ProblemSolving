#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in pairs.values():
                stack.append(bracket)
            elif bracket in pairs:
                if not stack or stack.pop() != pairs[bracket]:
                    return False
            else:
                return False

        return len(stack) == 0
        
        
# @lc code=end
sol=Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))