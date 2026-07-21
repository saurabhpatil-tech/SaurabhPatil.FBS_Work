# Q3. Write a program to input angles of triangle and check wheather the Triangle is valid or not :

a1 =int(input("Enter Angle 1 :"))
a2 =int(input("Enter Angle 2 :"))
a3 =int(input("Enter Angle 3 :"))

if ( a1+a2+a3 == 180 ):
    print("Triangle is Valid ")
else:
    print("Triangle is InValid")