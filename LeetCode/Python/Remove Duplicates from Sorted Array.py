class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1=list(set(nums))
        print(nums1)
        nums[:]=nums1[:]
        nums.sort()