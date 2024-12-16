import csv


list1 = []
list2 = []

with open('numbers1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for n1, n2 in csv_reader:
        list1.append(n1)
        list2.append(n2)

list1.sort()
list2.sort()

distance = 0

similarity = 0
second_list_follow = 0

for x in range(len(list1)):
    list1_num = int(list1[x])
    list2_num = int(list2[x])
    
    distance = abs(list1_num - list2_num) + distance

    sim_count = 0
    while int(list2[second_list_follow]) <= list1_num:
        if int(list2[second_list_follow]) == list1_num:
            sim_count += 1
        second_list_follow += 1
    
    similarity = similarity + (sim_count * list1_num)
    sim_count = 0



print(similarity)