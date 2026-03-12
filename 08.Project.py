lines = []

file = open("constitution.txt", "r")

for line in file:
    line = line.rstrip()
    lines.append(line)
file.close()

while True:
    term = input("Enter search term: ")
    if term == "":
        break
    i = 0

    while i < len(lines):

        if term.lower() in lines[i].lower():

            start = i
            while start > 0 and lines[start] != "":
                start = start - 1

            end = i
            while end < len(lines) and lines[end] != "":
                end = end + 1

            j = start
            while j < end:
                print("Line", j + 1, ":", lines[j])
                j = j + 1
            print()

            i = end
        else:
            i = i + 1