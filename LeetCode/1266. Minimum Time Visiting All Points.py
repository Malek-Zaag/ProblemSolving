from math import floor, sqrt
import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    n = list(map(int, input().split()))
    points=[n[i:i+2] for i in range(0,len(n),2)]
    result=0
    for i in range(len(points)-1):
        result+=max(abs(points[i][0] - points[i+1][0]) ,abs(points[i][1] -points[i+1][1]))
    return result


for _ in range(int(input())):
    print(solve())