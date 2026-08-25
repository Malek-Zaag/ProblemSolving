class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = max(candies)
        res=[]
        for i in candies:
            if i+ extraCandies >= max:
                max = i + extraCandies
                res.append(True)
        return res
    
sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))
print(sol.kidsWithCandies([4,2,1,1,2],1))