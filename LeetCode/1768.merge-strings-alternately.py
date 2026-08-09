class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,res=0,0,""
        n,m = len(word1),len(word2)
        while i < n and j < m:
            res+= word1[i]
            res+= word2[j]
            i+=1
            j+=1
        res+=word1[i:]
        res+=word2[j:]
        return res
    

sol= Solution()
print(sol.mergeAlternately("abc","pqr"))
print(sol.mergeAlternately("ab","pqrs"))
print(sol.mergeAlternately("abcd","pq"))