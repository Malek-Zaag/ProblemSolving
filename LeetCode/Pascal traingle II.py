
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    n = int(input())
    tab= [[1], [1,1]]      
    for i in range(2, n+1):
        row=[1]
        for j in  range(1, n):
            row.append( tab[i-1] [ j-1] + tab[i-1][j] )
        row.append(1)
        
        tab.append(row)
    return (tab[n-1])


for _ in range(int(input())):
    print(solve())