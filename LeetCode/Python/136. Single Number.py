import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")


import collections
def solve():
    nums = list(map(int, input().split()))
    counter=collections.Counter(nums)
    for i in counter :
         if counter.get(i) ==1 :
             return i
    return None


for _ in range(int(input())):
    print(solve())