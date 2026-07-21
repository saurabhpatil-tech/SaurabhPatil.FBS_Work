# Q9. Input 5 subject marks from user and display grade (eg. First class , Second class....):

s1 = int(input("Enter marks of Data analytics :"))
s2 = int(input("Enter marks of Data Science :"))
s3 = int(input("Enter marks of Computer :"))
s4 = int(input("Enter marks of Math :"))
s5 = int(input("Enter marks of Science :"))

Obtained_marks = s1 + s2 + s3 + s4 + s5
total_marks = 500

Per = Obtained_marks / total_marks * 100

print("Percentage :",Per)

if (Per >= 85):
    print("First class")
elif (Per >= 70):
    print("Second class")
elif (Per >= 55):
    print("Third class")
elif (Per >= 35):
    print("Pass")
else:
    print("Fail")