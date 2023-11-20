class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        shortest_len =len(strs[0])
        for i in strs[1:]:
            shortest_len=min(shortest_len,len(i))         
        output=""
        for j in range(shortest_len):
            current=strs[0][j]
            for i in range(len(strs)):
                if strs[i][j]!= current:
                    return output
            output+=current         
        return (output)