# Q6. WAP to check if a given number is prime or not :

num = int(input("Enter Number :"))

if ( num > 1 ):

    for i in range (2, num):   
        
        if (num % i == 0):
            print(f"{num} is not Prime Number ")
            break 
    else:
        print(f"{num} is a Prime Number")

else:
    print(f"{num} is not Prime Number")