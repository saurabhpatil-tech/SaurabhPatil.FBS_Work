# Q8. WAP to find which numbers are divisible by 7 and multiple of 5 in given range :

start = int(input("Enter Start:"))
end = int(input("Enter end:"))

for i in range (start , end+1):
    
    if ( i % 7 == 0 and i % 5 == 0 ):
        print("These Numbers are divisible by 7 and multiple by 5 :",i)
