import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= collections.Counter(nums)
        print(dict(count))
        for j in dict(count).values():
            if j > len(nums) /2 :
                value = {i for i in dict(count) if dict(count)[i]==j}
                print(type(value))
        return(list(value)[0])