import sys
import re
import io
import collections
import pprint
from copy import deepcopy
import functools

# Increase the recursion limit
sys.setrecursionlimit(10000)


with open("advent11.txt", "r") as f:
    line = f.readline()

ex = """125 17"""

# line = io.StringIO(ex)
# line = line.readline()

class Node:
    def __init__(self, value=None):
        self.value = value  
        self.next = None 

head = Node()
tmp = head

for num in line.split(" "):
    new = Node(int(num))
    tmp.next = new

    tmp = tmp.next
    
# nu_tmp = head.next
# while nu_tmp != None:
#     print(nu_tmp.value)
#     nu_tmp = nu_tmp.next



def is_even(value):
    return len(str(value)) % 2 == 0

def split_even(value):
    str_value = str(value)
    mid = len(str_value) // 2
    num1 = int(str_value[:mid])
    num2 = int(str_value[mid:])
    return num1, num2


# split_even(1234567891)

count = 0
while count < 25:
    tmp_follow = head.next
    
    while tmp_follow != None:
        # print("current value", tmp_follow.value)

        if tmp_follow.value == 0: # Rule 1: if 0 make 1
            tmp_follow.value = 1
        elif is_even(tmp_follow.value):
            num1, num2 = split_even(tmp_follow.value)
            # print("nums:", num1, num2)
            tmp_follow.value = num1 # Replace the current node
            hold = tmp_follow.next # Not to lose the list

            new_node = Node(num2) # Attach the half
            
            tmp_follow.next = new_node
            new_node.next = hold

            tmp_follow = tmp_follow.next
        else:
            value = int(tmp_follow.value)
            tmp_follow.value = value * 2024
            
        # print("new value", tmp_follow.value)
        tmp_follow = tmp_follow.next
    
    count += 1


final_follow = head.next
final_count = 0

while final_follow != None:
    final_count += 1
    print(final_follow.value)
    final_follow = final_follow.next

print(final_count)

@functools.cache
def ans(x,n):
    if n == 0:
        return 1
    if x == 0:
        result = ans(1, n-1)
    elif len(str(x)) % 2 ==0:
        x = str(x)
        result = 0
        result += ans(int(x[:len(x) // 2]), n - 1)
        result += ans(int(x[len(x) // 2:]), n - 1)
    else:
        result = ans(2024 * x, n - 1)
    return result

res = 0
for x in line.split(" "):
    x = int(x)
    res += ans(x, 75)

print(res)
