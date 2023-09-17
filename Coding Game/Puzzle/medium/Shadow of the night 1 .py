import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
maxx,maxy= w-1,h-1
minx = miny  = 0

while True:
    bomb_dir = input()
    if bomb_dir.find("U")>-1:
        maxy = y0 - 1
    elif bomb_dir.find("D")>-1:
        miny = y0 + 1
    if bomb_dir.find("L")>-1:
        maxx = x0 - 1
    elif bomb_dir.find("R")>-1:
        minx =x0 + 1
    x0 = minx + math.ceil((maxx  - minx)/2)
    y0 = miny + math.ceil((maxy  - miny)/2)
    # the location of the next window Batman should jump to.
    print("{0} {1}".format(int(x0), int(y0)))