import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    arr = list(map(int, input().split()))
    import collections
    counter= collections.Counter(arr)
    li=list(counter.values())
    for i,j in enumerate(li):
        if li.index(j) != i :
            return False
    return True


for _ in range(int(input())):
    print(solve())