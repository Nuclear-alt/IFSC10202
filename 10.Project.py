class Student:
    def __init__(self, firstname, lastname, tnumber, scores):

        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = scores  # list of strings (may contain empty values)

    def RunningAverage(self):
        valid_scores = [float(score) for score in self.Grades if score.strip() != ""]
        if len(valid_scores) == 0:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        total_scores = []
        for score in self.Grades:
            if score.strip() == "":
                total_scores.append(0.0)
            else:
                total_scores.append(float(score))

        if len(total_scores) == 0:
            return 0.0
        return sum(total_scores) / len(total_scores)

    def LetterGrade(self):
        avg = self.TotalAverage()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

def main():
    print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
    print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
    print("-" * 72)

    with open("10.Project Student Scores.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            firstname = parts[0]
            lastname = parts[1]
            tnumber = parts[2]
            scores = parts[3:]

            student = Student(firstname, lastname, tnumber, scores)

            running_avg = student.RunningAverage()
            total_avg = student.TotalAverage()
            letter = student.LetterGrade()

            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{running_avg:>12.2f} {total_avg:>12.2f} {letter:>12}")

if __name__ == "__main__":
    main()