import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")


def solve():
    s = list(input())
    l,  r= 0, len(s)-1 
    vowels=['A','E','I','O','U']
    while l < r :
        if s[r].upper() in vowels and s[l].upper() in vowels:                 
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        elif s[r].upper() in vowels and s[l].upper() not in vowels:
            l+=1
        elif s[r].upper() not in vowels and s[l].upper() in vowels:      
            r-=1
        else :
            l+=1
            r-=1
    return "".join(s)


for _ in range(int(input())):
    print(solve())