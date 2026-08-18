
# Q2. Write a recursive function to check whether a number is an Armstrong number.


def armstrong(n):
    
    if n == 0:
        return 0

    digit = n % 10
    return digit**count + armstrong(n // 10)


num = int(input("Enter a number: "))
count = len(str(num))
res = armstrong(num)


if res == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")