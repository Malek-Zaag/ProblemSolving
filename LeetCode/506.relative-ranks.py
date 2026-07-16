#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h={}
        score_sorted= sorted(score,reverse=True)
        medals=["Gold Medal","Silver Medal","Bronze Medal"]
        h={j: medals[i] if i<3 else str(i+1) for i,j in enumerate(score_sorted)}
        return [h[i] for i in score]
            
            
        
# @lc code=end

