import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

def man(array):
    answer=[1]*len(array)   
    prefix=1 
    for i in range(len(array)):
        answer[i]= prefix
        prefix*=array[i] 
    postfix=1
    for i in range(len(array) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]         
    return(answer)


for i in range(t):
    nums=[int(i) for i in input().split(',')]
    answer=man(nums)
    print(answer)