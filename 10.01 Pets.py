class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

pets = []

with open("10.01 Pets.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        pet = Pet()
        pet.name = data[0].strip()
        pet.type = data[1].strip()
        pet.age = int(data[2].strip())

        pets.append(pet)

print("{:<10}{:<10}{:<5}".format("Name", "Type", "Age"))

for pet in pets:
    print("{:<10}{:<10}{:<5}".format(pet.name, pet.type, pet.age))