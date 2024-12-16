import re
import io
import pprint
import sys

# Increase the recursion limit
sys.setrecursionlimit(10000)

with open("advent15.txt", "r") as f:
    lines = f.read()

# Example input
ex = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# lines = io.StringIO(ex)
# lines = lines.read()

robot_map, directions = lines.split("\n\n")

grid = []
for line in robot_map.split("\n"):
    char_list = []

    for char in line.strip():
        char_list.append(char)
    
    grid.append(char_list)

ROW = len(grid)
COL = len(grid[0])

robot_location = []
for row in range(ROW):
    for col in range(COL):
        if grid[row][col] == '@':
            robot_location = [row,col]


def direction_helper(row,col,direction):
    if direction == "^":
        row = row - 1
        col = col
    elif direction == ">":
        row = row
        col = col + 1
    elif direction == "v":
        row = row + 1
        col = col
    elif direction == "<":
        row = row
        col = col - 1
    
    return row,col

pprint.pprint(grid)

def dfs(row, col, direction):
    if grid[row][col] == "#":
        return False
    elif grid[row][col] == ".":
        grid[row][col] = "O"
        return True
    
    row, col = direction_helper(row,col,direction)
    spot = dfs(row, col, direction)

    if spot == True:
        grid[row][col] = "O"
    
    return spot

for line in directions.strip():
    x,y = robot_location
    move_x, move_y = direction_helper(x,y,line)
    if grid[move_x][move_y] == 'O': 
        if dfs(move_x,move_y,line):
            grid[x][y] = '.'
            x,y = direction_helper(x,y,line)
            grid[x][y] = '@'
            robot_location = [x,y]
    elif grid[move_x][move_y] == '.':
        grid[x][y] = '.'
        x,y = direction_helper(x,y,line)
        grid[x][y] = '@'
        robot_location = [x,y]
    elif grid[move_x][move_y] == '#':
        continue
    # pprint.pprint(grid)


pprint.pprint(grid)

res = 0
for i in range(ROW):
    for j in range(COL):
        if grid[i][j] == 'O':
            res += (100 * i) + j
    

print(res)

for line in directions.strip():
    dx,dy = {
        "^": (-1,0),
        "v": (1,0),
        ">": (0,1),
        "<": (0, -1)
    }[line]

    print(dx)
    print(line)