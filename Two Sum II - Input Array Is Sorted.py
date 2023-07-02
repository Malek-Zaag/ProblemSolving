import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())


for i in range(t):
    target=int(input())
    numbers=[int(i) for i in input().split(',')]
    first=0
    second=first+1
    while numbers[first] + numbers[second] != target:
        if numbers[first] == numbers[second] :
                first+=1
                second+=1
        if second== len(numbers)-1:
            first+=1
            second=first+1
        else : 
            second+=1
    print([first+1,second+1])
    