file = open("09.Project Distances.csv", "r")
table = []

for line in file:
    line = line.strip()
    row = line.split(",")
    table.append(row)
file.close()

for row in table:
    for item in row:
        print(item, "\t", end="")
    print()

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

row_index = -1
col_index = -1

i = 1
while i < len(table):
    if table[i][0] == from_city:
        row_index = i
        break
    i += 1

j = 1
while j < len(table[0]):
    if table[0][j] == to_city:
        col_index = j
        break
    j += 1

if row_index == -1:
    print("Invalid From City")
elif col_index == -1:
    print("Invalid To City")
else:
    distance = table[row_index][col_index]
    print(from_city, "to", to_city, "-", distance, "miles")