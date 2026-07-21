# Q8. Write a Program to prompt the user to enter UserId and Password ,After verifying them display 4 digit random number and ask the user to enter the same. if user enters the same number then show him success message otherwise failed. (Something like captcha) :

import random 

UserId = input("Enter the User Id :")
Password = input("Enter the Password :")

if UserId == 'Saurabh' and Password == '1234' :

    captch = random.randint(1000,9999)
    print(f'Your captcha={captch}')

    chuser = int(input("Enter the Captcha :"))

    if chuser == captch :
        print("User Login Successfully ")
    else:
        print("Invalid Captcha")
else:
    print("Invalid UserId & Password ")