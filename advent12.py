import sys
import re
import io
import collections
import pprint
from copy import deepcopy
import functools

# Increase the recursion limit
sys.setrecursionlimit(10000)


with open("advent12.txt", "r") as f:
    lines = f.readlines()

ex = """AAAA
BBCD
BBCC
EEEC"""

lines = io.StringIO(ex)
lines = lines.readlines()

grid = []
for line in lines:
    char_list = []

    for char in line.strip():
        char_list.append(char)
    
    grid.append(char_list)

# pprint.pprint(grid)

visited_peri = set()
def dfs_peri(row, col, value):
    if row not in range(ROW) or col not in range(COL):
        return 1
    
    if (row, col) in visited_peri and grid[row][col] == value:
        return 0

    if grid[row][col] != value:
        return 1
    
    visited_peri.add((row,col))

    return (dfs_peri(row + 1, col, value) +
        dfs_peri(row, col + 1, value) + 
        dfs_peri(row - 1, col, value) + 
        dfs_peri(row, col - 1, value))


visited_area = set()
def dfs_area(row, col, value):
    if row not in range(ROW) or col not in range(COL):
        return 0
    
    if (row, col) in visited_area and grid[row][col] == value:
        return 0

    if grid[row][col] == value:
        visited_area.add((row,col))
        return 1 + (dfs_area(row + 1, col, value) +
            dfs_area(row, col + 1, value) + 
            dfs_area(row - 1, col, value) + 
            dfs_area(row, col - 1, value))
    
    
    if grid[row][col] != value:
        return 0


visited_peri_2 = set()
def dfs_peri_2(row, col, value):
    if row not in range(ROW) or col not in range(COL):
        if (row, value) not in visited_peri_2 and (value, col) not in visited_peri_2:
            visited_peri_2.add((row, value))
            visited_peri_2.add((value, col))
            return 1
        else:
            return 0
    
    if (row, col) in visited_peri_2 and grid[row][col] == value:
        return 0

    if grid[row][col] != value:
        if (row, value, grid[row][col]) not in visited_peri_2 and (value, col, grid[row][col]) not in visited_peri_2:
            visited_peri_2.add((row, value, grid[row][col]))
            visited_peri_2.add((value, col, grid[row][col]))
            return 1
        else:
            return 0
    
    visited_peri_2.add((row,col))

    return (dfs_peri_2(row + 1, col, value) +
        dfs_peri_2(row, col + 1, value) + 
        dfs_peri_2(row - 1, col, value) + 
        dfs_peri_2(row, col - 1, value))


ROW = len(grid)
COL = len(grid[0])

peri = 0
area = 0
total_ap = 0

for row in range(ROW):
    for col in range(COL):
        if (row, col) not in visited_peri_2:
            # peri = dfs_peri(row, col, grid[row][col])
            # print(grid[row][col], ": ", peri)
            
            peri_p2 = dfs_peri_2(row, col, grid[row][col])
            print(grid[row][col], ": ", peri_p2)

            area = dfs_area(row, col, grid[row][col])
            print(grid[row][col], ": ", area)

            plot_ap = area * peri
            total_ap += plot_ap
            peri = 0
            peri_p2 = 0
            area = 0

# print(total_ap)
print(visited_peri_2)