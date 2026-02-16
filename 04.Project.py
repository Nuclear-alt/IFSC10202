H = int(input("Enter maximum height: "))
for i in range(1, H + 1):
    for r in range(1, i + 1):
        print("*", end="")
    print()

for i in range(H - 1, 0, - 1):
    for r in range(1, i + 1):
        print("*", end="")
    print()