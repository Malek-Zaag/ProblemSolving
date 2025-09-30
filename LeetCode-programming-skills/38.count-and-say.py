#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def helper(self,n):
        res=[]
        l=len(n)
        for i in range(0,l-1):
            count=1
            mini_res=[1,n[i]]
            for j in range(i+1,l):
                if n[j] != n[i]:
                    res.append(mini_res)
                    print(mini_res)
                    break
                else : 
                    count+=1
                    mini_res[0]=count
                    print(mini_res)
        return res
    
    def converter(self,arr):
        res=""
        for i in arr: 
            res+=i[0] + i[1]
        return res
    
    def countAndSay(self, n: int) -> str:
        result="1"
        for _ in range(n-1):
            result=self.converter(self.helper(result))
        return result
        

         
# @lc code=end

