import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    strs=input().split(",")
    if len(strs) == 1 or len(strs)==0: print([strs])
    h=dict()
    for i in strs:
        if (h.get(''.join(sorted(i)))== None): 
            h[''.join(sorted(i))]=[i]
        else : h[''.join(sorted(i))].append(i)
    print(list(h.values()))