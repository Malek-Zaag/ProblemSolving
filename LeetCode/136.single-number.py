#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import collections
from itertools import count
from typing import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter=collections.Counter(nums)
        return [i for i in list(counter.keys()) if counter.get(i) == 1][0]
# @lc code=end

