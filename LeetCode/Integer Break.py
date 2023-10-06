
import collections
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    c=collections.Counter(nums)
    for i in c:
        if c[i] ==1 : return i


for _ in range(int(input())):
    print(solve())