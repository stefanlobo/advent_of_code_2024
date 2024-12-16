import sys
import re
import io

# Increase the recursion limit
sys.setrecursionlimit(10000)

calc_nums = []
with open("advent7.txt", "r") as f:
    lines = f.readlines()

# Sample Ex
ex = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
# lines = io.StringIO(ex)
# lines = lines.readlines()


def dfs(numbers, index, in_total, final):
    if index >= len(numbers):
        return False
        
    total1 = in_total + numbers[index]
    total2 = in_total * numbers[index]
    total3 = int(str(in_total) + str(numbers[index])) 

    if index == (len(numbers) - 1) and total1 == final:
        return True
    if index == (len(numbers) - 1) and total2 == final:
        return True
    if index == (len(numbers) - 1) and total3 == final: # Part 3
        return True
    
    return (dfs(numbers, index + 1, total1, final) or dfs(numbers, index + 1, total2, final) or
        dfs(numbers, index + 1, total3, final))

    

    
total = 0
for line in lines:
    numbers = re.findall("\d+", line)
    numbers = [int(number) for number in numbers]
    treasure = numbers[0]
    if dfs(numbers[2:], 0, numbers[1], treasure) == True:
        total = treasure + total

print(total)
