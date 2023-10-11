import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")

from collections import Counter

def solve():
    nums = list(map(int, input().split()))
    k=int(input())
    return (lambda c: sum(min(c[n], c[k-n]) for n in c))(Counter(nums))//2


for _ in range(int(input())):
    print(solve())