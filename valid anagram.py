import sys 



sys.stdin=open("./in.txt","r")
sys.stdout=open("./out.txt","w")


t=int(input())
for i in range(t):
    s,t=input().split(",")
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    print (dic1 == dic2) 