
# Q11. Write a program to print all numbers which are divisible by m and n in the list.


li = [10, 22, 12, 18, 24, 50, 60, 40]

m = int(input("Emter value of m :"))
n = int(input("Emter value of n :"))

for num in li:

    if num % m == 0 and num % n == 0:
        print(num)
