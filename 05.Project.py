start_and_end = int(input("Enter starting value: "))

for i in range(1, 10000):
    Number = i
    temp = Number
    digits = 0

    while temp > 0:
        temp //= 10
        digits += 1
    
    totle = 0
    temp = Number

    while temp > 0:
        digit = temp % 10
        totle += digit ** digits
        temp //= 10

    if totle == Number:
        print(Number)