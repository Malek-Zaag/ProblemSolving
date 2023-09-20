class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        output=[]
        for i in s[::-1]:
            if i !=" " and i !="" :
                output.append(i)
        print(output)
        return(" ".join(output))