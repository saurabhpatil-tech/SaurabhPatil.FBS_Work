# Q1. Write a program to prompt user to enter userid and password.
# If Id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times. After that program to terminate.


UserId = input("Enter the User Id : ")
Password = input("Enter the Password : ")

for i in range(3):

    if UserId == "Saurabh" and Password == "1234":
        print("Login Successful")
        break
    else:
        print("Incorrect ")

    if i < 3:
        UserId = input("Enter the User Id : ")
        Password = input("Enter the Password : ")

else:
    print("Access Denied")