value = input("Enter a number (CR to quit): ")
if value != "":
    maximun = int(value)
    while value != "":
        if int(value) > maximun:
        maximun = int(value)
    value = input("Enter a number (CR to quit): ")
print("Maximun: {}".format(maximun))