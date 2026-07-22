# Q9. WAP to print all numbers in a range divisible by a given number :

start = int(input("Enter Start Number :"))
end = int(input("Enter End Number :"))
num = int(input("Enter Divisor :"))

for i in range (start , end+1):

    if ( i % num == 0):
        print(i)