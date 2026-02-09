sequencesum = 0
sequencecount = 0
value = input("Enter a number (CR to quit): ")
while value != '':
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a number (CR to quit): ")
if sequencecount != 0:
    sequenceaverage = sequencesum / sequencecount
    print("Averahe: {}".format(sequenceaverage))
else:
    print("Sequencesum is 0")