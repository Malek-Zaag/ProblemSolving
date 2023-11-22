import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))
    import collections
    count= collections.Counter(nums)
    for i in list(count.keys()):
        if count.get(i)==1: 
            return i
    return None


for _ in range(int(input())):
    print(solve())