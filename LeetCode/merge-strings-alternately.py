import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    str1, str2= input().split()
    n1,n2 = len(str1), len(str2)
    i,j= 0,0
    res="" 
    while i < n1 or j < n2:
        if i < n1 and j < n2:
            res+=str1[i] + str2[j]
            i+=1
            j+=1
        elif i < n1 and j >=n2:
            res+= str1[i]
            i+=1
        elif i >= n1 and j < n2:
            res+= str2[j]
            j+=1
    return res

for _ in range(int(input())):
    print(solve())