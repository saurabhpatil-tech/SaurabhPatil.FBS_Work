# Q8 .  Write a program to swap two numbers using third variable :

x = int(input("Enter value of x :"))
y = int(input("Enter value of y :"))

temp = x
x = y
y = temp

print(f"After Swapping : x={x}  and  y={y} " )