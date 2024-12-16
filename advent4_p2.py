import re

word_search = []
with open("wordsearch.txt", "r") as f:
    x = f.readlines()

for line in x:
    char_list = []
    for col in line.strip():
        char_list.append(col)

    word_search.append(char_list)


def island(prev, row, col, word_search, ROW, COL, direction):
    if row < 0 or col < 0 or row >= len(word_search) or col >= len(word_search[0]):
        return 0

    if direction == "br":
        new_row = row - 2
        new_col = col - 2
    elif direction == "bl":
        new_row = row + 2
        new_col = col + 2
    elif direction == "tr":
        new_row = row - 2 
        new_col = col + 2
    elif direction == "tl":
        new_row = row + 2
        new_col = col - 2 

    if prev == "A":
        if word_search[row][col] == "M":
            return island("MA", new_row, new_col, word_search, ROW, COL, direction)
        if word_search[row][col] == "S":
            return island("SA", new_row, new_col, word_search, ROW, COL, direction)
    elif prev == "MA":
        if word_search[row][col] == "S":
            return 1
    elif prev == "SA":
        if word_search[row][col] == "M":
            return 1
        
    return 0


ROW = len(word_search)
COL = len(word_search[0])
total = 0

for row in range(ROW):
    for col in range(COL):
        if word_search[row][col] == "A":
            total += 1 if (island("A", row + 1, col + 1, word_search, ROW, COL, "br")
                + island("A", row - 1, col - 1, word_search, ROW, COL, "bl")
                + island("A", row + 1, col - 1, word_search, ROW, COL, "tr")
                + island("A", row - 1, col + 1, word_search, ROW, COL, "tl") == 4) else 0

print(total)
