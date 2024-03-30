import sys 
sys.stdin=open("./Leetcode/in.txt","r")
sys.stdout=open("./Leetcode/out.txt","w")



def solve():
    nums = list(map(int, input().split()))  
    result=[]
    start, end=nums[0], nums[0]
    for i,j in enumerate(nums[1:len(nums)+2]):        
        if j == nums[i]+1:
            end=j
        else: 
            if start == end: 
                result.append(str(start))
            else: 
                result.append(str(start) + "->" + str(end))          
            start,end=j,j
        if i==len(nums)-2:
            if start == end: 
                result.append(str(start))
            else: 
                result.append(str(start) + "->" + str(end))  
            

            
    print(result)
    
    
    
    
for _ in range(int(input())):
    solve()