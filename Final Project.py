# Step 1, Employee Class
class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):
        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

# Step 2, EmployeeList Class
class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []

    def ReadEmployeeFile(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 7:
                        emp = Employee(
                            parts[0].strip(),
                            parts[1].strip(),
                            parts[2].strip(),
                            parts[3].strip(),
                            parts[4].strip(),
                            parts[5].strip(),
                            parts[6].strip()
                        )
                        self.employees.append(emp)
        except FileNotFoundError:
            print("File not found. Starting with empty list.")

    def WriteEmployeeFile(self):
        with open(self.filename, "w") as file:
            for e in self.employees:
                line = f"{e.emp_num},{e.first},{e.last},{e.address},{e.city},{e.state},{e.zip_code}\n"
                file.write(line)
        print("File saved.")

    def DisplayEmployeeList(self):
        print("\nEmployee         First           Last            Address         City            State           Zip")
        print("Number           Name            Name")
        print("-" * 95)

        for e in self.employees:
            print(f"{e.emp_num:<15}{e.first:<15}{e.last:<15}{e.address:<15}{e.city:<15}{e.state:<15}{e.zip_code:<15}")

    def FindEmployee(self, emp_num):
        for i in range(len(self.employees)):
            if self.employees[i].emp_num == emp_num:
                return i
        return -1

    def NextEmployeeNumber(self):
        if len(self.employees) == 0:
            return 1
        return self.employees[-1].emp_num + 1

    def AddEmployee(self, first, last, address, city, state, zip_code):
        emp_num = self.NextEmployeeNumber()
        emp = Employee(emp_num, first, last, address, city, state, zip_code)
        self.employees.append(emp)
        print("Employee Added")

    def DeleteEmployee(self, emp_num):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Employee not found")
        else:
            del self.employees[index]
            print("Employee Deleted")

    def UpdateEmployee(self, emp_num, field, value):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Employee not found")
            return

        emp = self.employees[index]

        if field == "F":
            emp.first = value
        elif field == "L":
            emp.last = value
        elif field == "A":
            emp.address = value
        elif field == "C":
            emp.city = value
        elif field == "S":
            if validate_state(value):
                emp.state = value
            else:
                print("Invalid state")
        elif field == "Z":
            if validate_zip(value):
                emp.zip_code = value
            else:
                print("Invalid zip")

# Step 3, Validation Functions
def validate_state(state):
    return len(state) == 2 and state.isupper()

def validate_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required.")

# Step 4, Main Program
def main():
    emp_list = EmployeeList("Final Project Employees.txt")
    emp_list.ReadEmployeeFile()

    while True:
        print("\n(A)dd (D)elete (C)hange (P)rint (S)ave (Q)uit")
        choice = input("Enter Selection: ").upper()

        if choice == "A":
            first = get_non_empty("Enter First Name: ")
            last = get_non_empty("Enter Last Name: ")
            address = get_non_empty("Enter Address: ")
            city = get_non_empty("Enter City: ")

            while True:
                state = input("Enter State: ")
                if validate_state(state):
                    break
                print("State must be 2 uppercase letters")

            while True:
                zip_code = input("Enter Zip: ")
                if validate_zip(zip_code):
                    break
                print("Zip must be 5 digits")

            emp_list.AddEmployee(first, last, address, city, state, zip_code)

        elif choice == "D":
            try:
                emp_num = int(input("Enter Employee Number: "))
                emp_list.DeleteEmployee(emp_num)
            except:
                print("Invalid number")

        elif choice == "C":
            try:
                emp_num = int(input("Enter Employee Number: "))
                if emp_list.FindEmployee(emp_num) == -1:
                    print("Employee not found")
                    continue

                while True:
                    print("\n(F)irst (L)ast (A)ddress (C)ity (S)tate (Z)ip (B)ack")
                    field = input("Enter Selection: ").upper()

                    if field == "B":
                        break

                    value = input("Enter new value: ")
                    emp_list.UpdateEmployee(emp_num, field, value)

            except:
                print("Invalid input")

        elif choice == "P":
            emp_list.DisplayEmployeeList()

        elif choice == "S":
            emp_list.WriteEmployeeFile()

        elif choice == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid choice")

main()