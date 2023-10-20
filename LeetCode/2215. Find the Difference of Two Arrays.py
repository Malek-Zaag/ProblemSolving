import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums1= list(map(int, input().split()))
    nums2= list(map(int, input().split()))
    res1=[]
    res2=[]
    for i in nums1:
        if i not in nums2 and i not in res1:
            res1.append(i)
    for j in nums2:
        if j not in nums1 and j not in res2:
            res2.append(j)
    return [res1,res2]

for _ in range(int(input())):
    print(solve())