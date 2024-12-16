import re

string1='mul('

with open("numbers3.txt", "r") as file:
    content = file.read()

total = 0

do_flag = True

for char_index in range(len(content)):
    l = char_index
    r = char_index + 4

    if content[l] == 'd':
        r_do = l + 4
        r_dont = l + 7
        print(content[l:r_do])
        if content[l:r_do] == 'do()':
            do_flag = True
        elif content[l:r_dont] == rf"don't()":
            do_flag = False

    if content[l:r] == string1 and do_flag == True:
        numbers1 = ""
        numbers2 = ""
        n1i = r
        if content[n1i].isdigit():
            while content[n1i].isdigit():
                numbers1 += content[n1i]
                n1i += 1
        
        if content[n1i] == ',':
            n1i += 1
            if content[n1i].isdigit():
                while content[n1i].isdigit():
                    numbers2 += content[n1i]
                    n1i += 1
        
        if content[n1i] == ')':
            if numbers1.isdigit() and numbers2.isdigit():
                numbers1 = int(numbers1)
                numbers2 = int(numbers2)
                print(numbers1, numbers2)
                total = total + (numbers1 * numbers2)

print(total)
        
