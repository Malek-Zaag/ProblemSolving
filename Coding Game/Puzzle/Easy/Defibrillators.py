import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(",","."))
lat = float(input().replace(",","."))
n = int(input())
tab=[]
defibs=[]
for i in range(n):
    defib = input().rsplit(";",2)
    defibs.append(defib[0])
    lat_b,lon_b=float(defib[2].replace(",",".")), float(defib[1].replace(",","."))
    x=(lon_b - lon) * math.cos((lat_b+lat) /2 )
    y=lat_b - lat
    d=pow(x**2 + y**2,0.5) *  6371
    tab.append(d)

print(defibs[tab.index(min(tab))].split(";")[1])