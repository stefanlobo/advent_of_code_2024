import re
import pandas as pd
import io
from collections import deque

ex = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

word_search = []
with open("advent5.txt", "r") as f:
    lines = f.readlines()

# For Example
# lines = io.StringIO(ex)
# lines = lines.readlines()

# Find the index of the first empty line
split_index = lines.index('\n')

# Split the lines into two parts
top_half = lines[:split_index]
bottom_half = lines[split_index+1:]

hashM = {}
hashD = {}
for line in top_half:
    x,y  = re.findall('\d+', line)
    if x not in hashM:
        hashM[x] = set()
    if y not in hashD:
        hashD[y] = set()
    hashM[x].add(y)
    hashD[y].add(x)

def p1(bottom_half):
    total = 0

    for line in bottom_half:
        line_split = [x.strip() for x in line.split(',')]
        print(line_split)
        middle = line_split[len(line_split) // 2]
        flag = False
        for num_index in range(len(line_split)):
            post = num_index + 1
            print(line_split[num_index])
            
            if post < len(line_split):
                print(line_split[post])
                if line_split[num_index] not in hashM:
                    flag = False
                    break
                elif line_split[post] not in hashM[line_split[num_index]]:
                    flag = False
                    break
                else:
                    flag = True
        
        if flag:
            # print(line_split)
            total += int(middle)

    return total

def count_values(num, hashmap):
    if num not in hashmap:
        return 0

    return len(hashmap.get(num, set()))

print(hashM)

def dfs(crs, visit, output, cur_line):
    if crs in visit:
        return True
    
    for pre in hashD.get(crs, set()):
        if pre in cur_line:
            dfs(pre, visit, output, cur_line)

    visit.add(crs)

    output.append(crs)
    return True


def p2(bottom_half):
    total = 0
    
    for line in bottom_half:
        line_split = [x.strip() for x in line.split(',')]
        ok = True

        for i, x in enumerate(line_split):
            for j, y in enumerate(line_split):
                if i<j and y in hashD.get(x, set()):
                    ok = False
        
        if ok == False:
            good = []
            visit = set()
            cur_line = set(line_split)

            for num in line_split:
                dfs(crs=num, visit=visit, output=good, cur_line=cur_line)

            middle = good[len(good) // 2]
            total += int(middle) 

    return total

# print(p1(bottom_half))
print(p2(bottom_half))