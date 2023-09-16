import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x, thor_y = initial_tx, initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction1=""
    direction2=""
    
    if light_y < thor_y :
        direction1 = "N"
        thor_y-=1
    elif thor_y < light_y :
        direction1 = "S"
        thor_y+=1
    if light_x < thor_x :
        direction2 = "W"
        thor_x-=1
    elif thor_x < light_x :
        direction2 = "E"
        thor_x+=1
    print(direction1+direction2)
