class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rsplit()
        print(s)
        return(len(s[-1]))