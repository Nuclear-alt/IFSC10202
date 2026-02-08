First_Number = float(input("Enter First Number: "))
Enter_Operator = input("Enter Operator (+, -, *, /): ")
Second_Number = float(input("Enter Second Number: "))

if Enter_Operator == "+":
    print(First_Number + Second_Number)
elif Enter_Operator == "-":
    print(First_Number - Second_Number)
elif Enter_Operator == "*":
    print(First_Number * Second_Number)
elif Enter_Operator == "/":
    if Second_Number != 0:
        print(First_Number / Second_Number)
else:
    print("Invalid Operator")