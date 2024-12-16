import csv


list1 = []
list2 = []

safe = 0
with open('numbers2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

# Find the maximum number of columns in any row
max_columns = max(len(row) for row in rows)

# Remove extra commas by ensuring all rows have the same number of columns
cleaned_rows = []
for row in rows:
    cleaned_row = [int(value) for value in row if value]  # Remove empty values
    cleaned_rows.append(cleaned_row)


def check(row):
    l = 0
    r = 1

    # Decreasing
    if row[l] > row[r]:
        while r < len(row) - 1:
            if row[l] > row[r] and (row[l] - row[r]) <= 3 and (row[l] - row[r]) >= 1:
                l += 1
                r += 1
            else:
                break

        if (r == len(row) - 1) and row[l] > row[r] and (row[l] - row[r]) <= 3 and (row[l] - row[r]) >= 1:
            print(row)
            return True

    # Increasing
    elif row[l] < row[r]:
        while r < len(row) - 1:
            if row[l] < row[r] and (row[r] - row[l]) <= 3 and (row[r] - row[l]) >= 1:
                l += 1
                r += 1
            else:
                break
        
        if (r == len(row) - 1) and row[l] < row[r] and (row[r] - row[l]) <= 3 and (row[r] - row[l]) >= 1:
            print(row)
            return True
    

for row in cleaned_rows:
    if check(row) or any(check(row[:i] + row[i+1:]) for i in range(len(row))):
        safe += 1

print(safe)