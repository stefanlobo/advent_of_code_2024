import sys
import re
import io
import collections
import pprint
from copy import deepcopy

# Increase the recursion limit
sys.setrecursionlimit(10000)


with open("advent10.txt", "r") as f:
    lines = f.readlines()

ex = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# lines = io.StringIO(ex)
# lines = lines.readlines()

grid = []

for line in lines:
    char_list = []
    for col in line.strip():
        col = int(col)
        char_list.append(col)

    grid.append(char_list)

# pprint.pprint(grid)

def dfs(row, col, last, visited):
    if row < 0 or col < 0 or row >= ROW or col >= COL:
        return 0
    
    value = grid[row][col]

    if (row, col) in visited:
        return 0
    
    if (last + 1) != value: return 0

    if value == 9 and last == 8: 
        visited.add((row, col))
        return 1


    result =  (dfs(row + 1, col, grid[row][col], visited) + 
            dfs(row, col + 1, grid[row][col], visited) +
            dfs(row - 1, col, grid[row][col], visited) + 
            dfs(row, col - 1, grid[row][col], visited))
    
    # visited.remove((row, col))

    return result

def dfs_p2(row, col, last):
    if row < 0 or col < 0 or row >= ROW or col >= COL:
        return 0
    
    value = grid[row][col]

    
    if (last + 1) != value: return 0

    if value == 9 and last == 8: 
        return 1


    result =  (dfs_p2(row + 1, col, grid[row][col]) + 
            dfs_p2(row, col + 1, grid[row][col]) +
            dfs_p2(row - 1, col, grid[row][col]) + 
            dfs_p2(row, col - 1, grid[row][col]))
    
    # visited.remove((row, col))

    return result

ROW = len(grid)
COL = len(grid[0])

count = 0
for x in range(ROW):
    for y in range(COL):
        if grid[x][y] == 0:
            count += dfs_p2(x, y, -1)

print(count)