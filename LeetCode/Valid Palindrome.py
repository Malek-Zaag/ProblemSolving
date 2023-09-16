import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())


for i in range(t):
    s=input()
    s=s.lower()
    l,r=0,len(s)-1
    ispalindrome=True
    while l<r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if (s[l]!=s[r]):
            ispalindrome=False
        r-=1
        l+=1
    print(ispalindrome)