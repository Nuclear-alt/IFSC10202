import os

# Step 1, Validation Helpers
def is_valid_state(state):
    return state.isalpha() and len(state) == 2 and state.isupper()

def is_vaild_zip(zip_code):
    return zip_code.isdighit() and len(zip_code) == 5

def is_not_empty(value):
    return value.strip() != ""

# Step 2, Empoloyee Class
class Employee:
    def _init_(self, emp_num, first, last, address, city, state, zip_code):
        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

# Step 3, Class Empoloyeelist
class Employesslist:
    def _init_(self, filename):
        self.filename = filename
        self.employess = []

    def ReadEmployeeFile(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as file:
            for line in file:
                parts = [P.strip() for P in line.split(",")]
                if len(parts) == 7:
                    emp = Employee(*parts)
                    self.employess.append(emp)
    
    