import re
import io

with open("advent14.txt", "r") as f:
    lines = f.read()
    
# Example input
ex = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# lines = io.StringIO(ex)
# lines = lines.read()

# quads = set([1,0], [0,1], [0,0], [1,1])
grid = [[0,0], [0,0]]
mid_x = 101 // 2
mid_y = 103 // 2


for line in lines.split("\n"):
    line.strip()
    x,y,xdelta, ydelta = map(int, re.findall("-?\d+", line))
    
    
    for i in range(100):
        x = (x + xdelta) % 101
        y = (y + ydelta) % 103

    if x < mid_x and y < mid_y:
        grid[0][0] += 1
    elif x > mid_x and y < mid_y:
        grid[1][0] += 1
    elif x < mid_x and y > mid_y:
        grid[0][1] += 1
    elif x > mid_x and y > mid_y:
        grid[1][1] += 1

res = 1
for x, y in grid:
    res *= x
    res *= y

print(res)