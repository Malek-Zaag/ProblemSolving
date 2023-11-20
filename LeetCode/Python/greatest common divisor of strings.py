import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    str1 , str2 = input().split()
    if str1 + str2 != str2 + str1:
        return ""
    from math import gcd
    return str1[:gcd(len(str1),len(str2))]


for _ in range(int(input())):
    print(solve())