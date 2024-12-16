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

    if direction == "right":
        new_row = row + 1
        new_col = col
    elif direction == "down":
        new_row = row
        new_col = col + 1
    elif direction == "br":
        new_row = row + 1
        new_col = col + 1
    elif direction == "left":
        new_row = row - 1
        new_col = col
    elif direction == "up":
        new_row = row
        new_col = col - 1
    elif direction == "bl":
        new_row = row - 1
        new_col = col - 1
    elif direction == "tr":
        new_row = row + 1
        new_col = col - 1
    elif direction == "tl":
        new_row = row - 1
        new_col = col + 1

    if prev == "X":
        if word_search[row][col] == "M":
            return island("XM", new_row, new_col, word_search, ROW, COL, direction)
    elif prev == "XM":
        if word_search[row][col] == "A":
            prev += "A"
            return island("XMA", new_row, new_col, word_search, ROW, COL, direction)
    elif prev == "XMA":
        if word_search[row][col] == "S":
            return 1

    return 0


ROW = len(word_search)
COL = len(word_search[0])
total = 0
xmas = ""

for row in range(ROW):
    for col in range(COL):
        if word_search[row][col] == "X":
            total += (
                island("X", row + 1, col, word_search, ROW, COL, "right")
                + island("X", row, col + 1, word_search, ROW, COL, "down")
                + island("X", row + 1, col + 1, word_search, ROW, COL, "br")
                + island("X", row - 1, col, word_search, ROW, COL, "left")
                + island("X", row, col - 1, word_search, ROW, COL, "up")
                + island("X", row - 1, col - 1, word_search, ROW, COL, "bl")
                + island("X", row + 1, col - 1, word_search, ROW, COL, "tr")
                + island("X", row - 1, col + 1, word_search, ROW, COL, "tl")
            )

print(total)
