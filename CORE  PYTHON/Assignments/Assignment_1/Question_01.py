# Q1 :- write a program to calculate the percentage of student based on marks of any 5 subjects : 

s1 = float(input("Enter marks of Computer:"))
s2 = float(input("Enter marks of Math:"))
s3 = float(input("Enter marks of Science:"))
s4 = float(input("Enter marks of English:"))
s5 = float(input("Enter marks of Data Analytics:"))

obtained_marks = s1+s2+s3+s4+s5
total_marks = 500

percentage = obtained_marks/total_marks * 100

print("Obtained Marks:",obtained_marks)
print("Percentage of marks of 5 subjects:",percentage)