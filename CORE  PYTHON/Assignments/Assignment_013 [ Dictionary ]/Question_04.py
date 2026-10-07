
# Q4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("Enter Number :"))

square = {}

for i in range(1, n + 1):
    square[i] = i * i

print(square)