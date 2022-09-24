from position import Position
from unit import Unit
import pawn
import knight
import bishop
import rook
import queen
import king

units = [[0]*16]*2
grid = [[0]*8]*8
    
#Piece Setup
file = open("units.txt")
pieces = file.readlines()

a = b = 0

for piece in pieces:
    ID, type, opp, points = piece.split()
    if (b >= 16):
        break
    
    units[a][b] = Unit(ID, type, points,0)
    print(units[a][b].getID(), units[a][b].getType(), units[a][b].getPoints())
    units[a + 1][b] = Unit(opp, type, points,0)
    print(units[a][b].getID(), units[a][b].getType(), units[a][b].getPoints())
    b += 1

file.close()  

#Board Setup