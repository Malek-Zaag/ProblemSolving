# import sys

# sys.stdin=open('./in.txt',"r")
def solve():
    n=int(input())
    rows=[int(j) for j in  input().split()]
    cols=[int(j) for j in  input().split()]
    rows.sort()
    cols.sort()
    sum1=n * rows[0] + sum(cols)
    sum2=n * cols[0] + sum(rows) 
    print(min(sum1,sum2))
        
    
       
        
for _ in range(int(input())):
    solve()