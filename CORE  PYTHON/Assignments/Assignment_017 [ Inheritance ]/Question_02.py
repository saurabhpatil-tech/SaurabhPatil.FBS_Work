
# Q2. 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self, StudentId=0, Name="", Age=0, Percentage=0):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Rank:", self.CalculateRank())

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.StudentId} - {self.Name} - {self.Age} - {self.Percentage}%"


class EnggStudent(Student):
    def __init__(self, StudentId=0, Name="", Age=0, Percentage=0,
                 Branch="", InternalMarks=0):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"{self.StudentId}  {self.Name} {self.Age}  "
                f"{self.Percentage} {self.Branch}  {self.InternalMarks}")


e1 = EnggStudent(101, "Saurabh", 21, 84.5, "Computer", 85)
e1.Display()
print(e1)