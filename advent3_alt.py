import re

with open("numbers3.txt") as f:
    s = f.read().strip()

x = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", s)

ans = 0

g = True
for y in x:
    res = 1
    if y =="do()":
        g=True
    elif y =="don't()":
        g=False
    else:
        if g:
            nums = re.findall("\d+", y)
            # print(nums)
            for num in nums:
                res = res * int(num)
            ans += res

            w,z = map(int, y[4:-1].split(","))
            print(w,z)

print(ans)