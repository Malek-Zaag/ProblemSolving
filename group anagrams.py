import sys 
sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")
t=int(input())

for i in range(t):
    strs=input().split(",")
    tab=[]
    if strs==[""]:
        print(tab)
    elif len(strs)==1:
        tab=[[strs[0]]]
        print(tab)
    else : 
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        print (final)        