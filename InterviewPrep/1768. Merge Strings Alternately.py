import os
import sys 

# print(os.listdir())
sys.stdin=open("in.txt","r")
sys.stdout=open("out.txt","w")

def solve():
  word1,word2= input().split()
  resultWord=""
  l1=len(word1)
  l2=len(word2)
  if l1 > l2:
    for i in range(l2):
      resultWord+=word1[i]+word2[i]
    resultWord+=word1[i+1:]
  elif l2 > l1:
    for i in range(l1):
      resultWord+=word1[i]+word2[i]
    resultWord+=word2[i+1:]
  else:
    for i in range(l1):
      resultWord+=word1[i]+word2[i]
  return resultWord


for _ in range(int(input())):
    print(solve())