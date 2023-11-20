import sys 
import os 

sys.stdin=open("./LeetCode/in.txt","r")
sys.stdout=open("./LeetCode/out.txt","w")

n=int(input())


def merge( nums1, m, nums2, n):
    if m==0:
        nums1[:]=nums2[:]
    elif n==0:
        nums1=nums1
    else:
        tab=nums1[:m]+nums2[:]
        tab.sort()
        tab=[int(str(i)) for i in tab]
        nums1[:]=tab[:]
    return tab

for i in range(n):
    nums1=[int(i) for i in input().split(",")]
    m=int(input())
    nums2=[int(i) for i in input().split(",")]
    n=int(input())    
    print(merge( nums1, m, nums2, n))
    