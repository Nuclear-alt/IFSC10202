sequencesum = 0
value = input("Enter a number (CR to quit): ")
while value != '':
    sequencesum += int(value)
    value = input("Enter a number (CR to quit): ")
print("Sum: {}".format(sequencesum))