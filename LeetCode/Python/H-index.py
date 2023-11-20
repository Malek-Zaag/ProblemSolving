class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1: return min(citations[0],1)
        citations.sort(reverse=True)
        print(citations)
        for i,j in enumerate(citations):
            if i >= j :
                return(i)
        return(len(citations))