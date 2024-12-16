import sys
import pprint
sys.setrecursionlimit(1000000)

with open("advent9.txt") as f:
    s = f.read().strip()


files = {}
disk = {}
next_disk_location = 0
next_is_fill = True
next_file_id = 0
for digit in s:
    length = int(digit)
    if next_is_fill:
        files[next_file_id] = (next_disk_location, length)
        for loc in range(length):
            disk[next_disk_location + loc] = next_file_id
        next_is_fill = False
        next_file_id += 1
    else:
        next_is_fill = True
    next_disk_location += length


disk_copy = disk.copy()
left = 0
right = max(disk_copy.keys())
while left < right:
    if right in disk_copy:
        file_id = disk_copy[right]
        del disk_copy[right]
        while left in disk_copy:
            left += 1
        disk_copy[left] = file_id
    right -= 1


ans = 0
for loc, file_id in disk_copy.items():
    ans += loc * file_id
print(ans)

print(next_file_id)
files_to_compact = list(range(next_file_id - 1, -1, -1))
# pprint.pprint(files_to_compact)
# pprint.pprint(files)
# pprint.pprint(disk)
for file_id in files_to_compact:
    insert_pos = 0
    while insert_pos < files[file_id][0]:
        if all(insert_pos + i not in disk for i in range(files[file_id][1])):
            for i in range(files[file_id][1]):
                del disk[files[file_id][0] + i]
                disk[insert_pos + i] = file_id
            break
        else:
            insert_pos += 1

ans = 0
for loc, file_id in disk.items():
    ans += loc * file_id
print(ans)