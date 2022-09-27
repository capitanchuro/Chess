import kivy
from position import Position
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

units = [[0 for i in range(16)] for j in range(2)]
grid = [[0 for i in range(8)] for j in range(8)]

# Board Setup
for row in range(0, 8):
    for col in range(0, 8):
        grid[row][col] = Position(0, 0, row, col)

# Piece Setup
file = open("units.txt")
pieces = file.readlines()

a = b = 0
r = c = 0

for piece in pieces:

    ID, name, opp, points = piece.split()
    
    if (name == 'RO'):
        units[a][b] = Rook(ID, name, points)
        units[a + 1][b] = Rook(opp, name, points)
    elif (name == 'KN'):
        units[a][b] = Knight(ID, name, points)
        units[a + 1][b] = Knight(opp, name, points)
    elif (name == 'BI'):
        units[a][b] = Bishop(ID, name, points)
        units[a + 1][b] = Bishop(opp, name, points)
    elif (name == 'QE'):
        units[a][b] = Queen(ID, name, points)
        units[a + 1][b] = Queen(opp, name, points)
    elif (name == 'KI'):
        units[a][b] = King(ID, name, points)
        units[a + 1][b] = King(opp, name, points)
    else:
        units[a][b] = Pawn(ID, name, points)
        units[a + 1][b] = Pawn(opp, name, points)

    if (c < 8 and r < 2):
        units[a][b].setPOS(grid[r][c])
        grid[r][c].setUnit(units[a][b])
        grid[r][c].setID(units[a][b].getID())

        units[a + 1][b].setPOS(grid[7 - r][c])
        grid[7 - r][c].setUnit(units[a + 1][b])
        grid[7 - r][c].setID(units[a + 1][b].getID())

        c += 1
    else:
        r += 1

        units[a][b].setPOS(grid[r][0])
        grid[r][0].setUnit(units[a][b])
        grid[r][0].setID(units[a][b].getID())

        units[a + 1][b].setPOS(grid[7 - r][0])
        grid[7 - r][0].setUnit(units[a + 1][b])
        grid[7 - r][0].setID(units[a + 1][b].getID())

        c = 1
    b += 1

file.close()

for row in range(8):
    for col in range(8):
        if (grid[row][col].getUnit() != 0):
            print('[' + grid[row][col].getUnit().getName() + ']', end='')
        else:
            print('[  ]', end='')
    print()
