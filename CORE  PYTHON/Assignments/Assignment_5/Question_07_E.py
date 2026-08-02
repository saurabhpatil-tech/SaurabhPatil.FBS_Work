# Q7. Write program to solve the following series:

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter Number: "))
num = int(input("Enter the Ending value : "))

sum = 0
sign = 1
dem = 1

for i in range(1, num + 1):

    sum += sign * (x ** i) / dem
    dem += 2    
    sign *= -1
    

print("Sum =", sum)