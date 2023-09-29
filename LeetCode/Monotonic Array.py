import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")


def solve():
    n = list(map(int, input().split()))
    res = sorted(n)
    if n == res or res == n[::-1]:
        print(True)
    else : print(False)


for _ in range(int(input())):
    solve()