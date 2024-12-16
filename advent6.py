import sys
from copy import deepcopy

# Increase the recursion limit
sys.setrecursionlimit(10000)

grounds = []
with open("advent6.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    char_list = []
    # print(line)
    for row in line.strip():
        char_list.append(row)

    grounds.append(char_list)


# Example usage
# grounds = [
#     ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
#     ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
# ]

grounds2 = deepcopy(grounds)

def direction_pointer(direction, row, col):
    if direction == 0: # up
        new_row = row - 1
        new_col = col
    elif direction == 1: # right
        new_row = row
        new_col = col + 1
    elif direction == 2: # down
        new_row = row + 1
        new_col = col
    elif direction == 3: # left
        new_row = row 
        new_col = col - 1 

    return new_row, new_col

def dfs(row, col, direction):
    if row < 0 or col < 0 or row >= len(grounds) or col >= len(grounds[0]):
        return
    
    if grounds[row][col] == '.' or grounds[row][col] == 'X':
        grounds[row][col] = 'X'
    
    # print(row,col)

    new_row, new_col = direction_pointer(direction, row, col)

    while (new_row >= 0 and new_col >= 0 and new_row < len(grounds) and new_col < len(grounds[0])) and grounds[new_row][new_col] == '#':
        direction = (direction + 1) % 4
        # print(grounds[new_row][new_col])
        # print(new_row, new_col)
        # print(direction)
        new_row, new_col = direction_pointer(direction, row, col)

    return dfs(new_row, new_col, direction)
    
ROW = len(grounds)
COL = len(grounds[0])
total = 0



for row in range(ROW):
    for col in range(COL):
        if grounds[row][col] == "^":
            start_row, start_col = row, col
            grounds[row][col] = "X"
            dfs(row, col, 0)

for row in range(ROW):
    for col in range(COL):
        if grounds[row][col] == "X":
            total += 1

# print(total)
# print(grounds)

def dfs2(row, col, direction):
    if row < 0 or col < 0 or row >= len(new_field) or col >= len(new_field[0]):
        return False
    
    if new_field[row][col] == '.' or new_field[row][col] == 'X':
        new_field[row][col] = 'X'
        if (row,col,direction) in visit:
            return True
        visit.add((row, col, direction))

    
    # print(row,col)

    new_row, new_col = direction_pointer(direction, row, col)

    while (new_row >= 0 and new_col >= 0 and new_row < len(new_field) and new_col < len(new_field[0])) and new_field[new_row][new_col] == '#':
        direction = (direction + 1) % 4
        # print(new_field[new_row][new_col])
        # print(new_row, new_col)
        # print(direction)
        new_row, new_col = direction_pointer(direction, row, col)
    
    return dfs2(new_row, new_col, direction)

loop = 0

# new_field = deepcopy(grounds2)

visit_ob = set()
for row in range(ROW):
    for col in range(COL):
        new_field = deepcopy(grounds2)
        if (new_field[row][col] != "#" and new_field[row][col] != "^") and (row,col) not in visit_ob:
            new_field[row][col] = "#"
            visit_ob.add((row,col))
            visit = set()
            if dfs2(start_row, start_col, 0):
                loop += 1
            # if row == 6 and col == 3:
            #     print(new_field)

print(loop) 