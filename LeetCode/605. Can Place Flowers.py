import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    flowerbed  = list(map(int, input().split()))
    n=int(input())
    i=1
    flowerbed[::]=[0] + flowerbed[::] + [0]
    while i < len(flowerbed)-1 and n > 0:
            if flowerbed[i] == 0 and flowerbed[i+1] ==0 and flowerbed[i-1] == 0:
                        flowerbed[i] =1
                        n-=1 
            i+=1
    print(flowerbed)
    if n > 0 : return False
    else : return True


for _ in range(int(input())):
    print(solve())