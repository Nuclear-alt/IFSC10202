First_file  = "06.Project Output File.txt"
Second_file = "06.Project Input File.txt"
third_file  = "06.Project Merge File.txt"

input_count = 0
merge_count = 0
output_count = 0

with open(First_file, "w") as output_file:
    with open(Second_file, "r") as input_file:
        for line in input_file:
            input_count += 1

            output_file.write(line)
            output_count += 1

            if "Insert Merge File Here" in line:
                