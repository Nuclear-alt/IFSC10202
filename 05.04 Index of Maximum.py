value = input("Enter a number (CR to quit): ")
if value != "":
    maximum = int(value)
    maximumindex = 1
    currentindex = 1
    while value != "":
        if int(value) > maximum:
        maximum = int(value)
        maximumindex = currentindex
    value = input("Enter a number (CR to quit): ")
    currentindex += 1
print("Maximun: {}".format(maximum))
print("Index of Maximum")
