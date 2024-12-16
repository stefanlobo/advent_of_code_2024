import sys
import re
import io
import collections
import pprint
from copy import deepcopy

# Increase the recursion limit
sys.setrecursionlimit(10000)

file_list = []
calc_nums = []
with open("advent9.txt", "r") as f:
    line = f.readline()

count = 0
count_free = 0
for x,y in enumerate(line):
    if x % 2 == 0:
        lenth_of_file = int(y)
        # print(lenth_of_file)
        while lenth_of_file > 0:
            file_list.append(count)
            lenth_of_file-=1
        count += 1
    else:
        lenth_of_file = int(y)
        while lenth_of_file > 0:
            file_list.append(".")
            lenth_of_file-=1
        count_free += 1

print(file_list)

file_list_p2 = deepcopy(file_list)

l,r = 0, len(file_list_p2) - 1

while l <= r:
    while file_list_p2[l] != ".":
        l += 1
    while file_list_p2[r] == ".":
        r -= 1
    
    if l < r:
        file_list_p2[l] = file_list_p2[r]
        file_list_p2[r] = "."

        l+=1
        r-=1

total = 0
for i, value in enumerate(file_list_p2):
    if value != ".":
        total+= (i * value)

print(total)


