import sys
import re
import io
import collections
import pprint
from copy import deepcopy

# Increase the recursion limit
sys.setrecursionlimit(10000)

calc_nums = []
with open("advent8.txt", "r") as f:
    lines = f.readlines()

# Sample Ex
ex = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
# lines = io.StringIO(ex)
# lines = lines.readlines()

grid = []
for line in lines:
    char_list = []
    count = 0
    for col in line.strip():
        char_list.append(col)
        count += 1

    grid.append(char_list)

hash_locations = collections.defaultdict(list)
# print(grid)

grid_p2 = deepcopy(grid)

ROW = len(grid)
COL = len(grid[0])

for x in range(ROW):
    for y in range(COL):
        if grid[x][y] != ".":
            char = grid[x][y]
            hash_locations[char].append([x,y])

for key in hash_locations.keys():
    for first in range(len(hash_locations[key])):
        for second in range(first + 1, len(hash_locations[key])):
            x1, y1 = hash_locations[key][first]
            x2, y2 = hash_locations[key][second]

            x_change = x2 - x1
            y_change = y2 - y1

            hash_one_x = x2 + x_change
            hash_one_y = y2 + y_change

            hash_two_x = x1 - x_change
            hash_two_y = y1 - y_change


            if (hash_one_x in range(ROW) and hash_one_y in range(COL) and grid[hash_one_x][hash_one_y] != "#"):
                grid[hash_one_x][hash_one_y] = "#"
            
            if hash_two_x in range(ROW) and hash_two_y in range(COL) and grid[hash_two_x][hash_two_y] != "#":
                grid[hash_two_x][hash_two_y] = "#"

count = 0
for x in range(ROW):
    for y in range(COL):
        if grid[x][y] == "#":
            count += 1

pprint.pprint(hash_locations)
pprint.pprint(grid)
print(count)

def p2(grid):
    for key in hash_locations.keys():
        for first in range(len(hash_locations[key])):
            for second in range(first + 1, len(hash_locations[key])):
                x1, y1 = hash_locations[key][first]
                x2, y2 = hash_locations[key][second]

                x_change = x2 - x1
                y_change = y2 - y1

                hash_one_x = x2 + x_change
                hash_one_y = y2 + y_change

                hash_two_x = x1 - x_change
                hash_two_y = y1 - y_change

                grid[x1][y1] = "#"
                grid[x2][y2] = "#"

                while (hash_one_x in range(ROW) and hash_one_y in range(COL)):
                    grid[hash_one_x][hash_one_y] = "#"
                    hash_one_x = hash_one_x + x_change
                    hash_one_y = hash_one_y + y_change
                
                while hash_two_x in range(ROW) and hash_two_y in range(COL):
                    grid[hash_two_x][hash_two_y] = "#"
                    hash_two_x = hash_two_x - x_change
                    hash_two_y = hash_two_y - y_change

p2(grid_p2)

count = 0
for x in range(ROW):
    for y in range(COL):
        if grid_p2[x][y] == "#":
            count += 1

pprint.pprint(grid_p2)
print(count)