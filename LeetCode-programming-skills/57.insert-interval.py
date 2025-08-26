#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        merge = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            merge.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        merge.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            merge.append(intervals[i])
            i += 1
        return merge
# @lc code=end

