import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    # n = list(map(int, input().split()))
    colors=list(input())
    if len (colors) <=2 : return False
    num_A=0
    num_B=0
    for i in range(1,len(colors) -1 ):
        if colors[i] == colors[i+1] == colors[i-1] == "A":
            num_A+=1
        elif colors[i] == colors[i+1] == colors[i-1] == "B":
            num_B+=1
    if num_A > num_B:
        return True
    else : return False
    # lock=0
    # i=1
    # while i <= len(colors) -1 :
    #     if lock==0 :
    #         if colors[i-1] == "A" and colors[i]=="A" and colors[i+1]=="A":
    #             colors.remove(colors[i])
    #             lock=1
    #         else : return False
    #     else :
    #         if colors[i-1] == "B" and colors[i]=="B" and colors[i+1]=="B":
    #             colors.remove(colors[i])
    #             lock=1
    #         else : return True
    


for _ in range(int(input())):
    print(solve())