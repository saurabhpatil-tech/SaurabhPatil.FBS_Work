# Q5. Sum of all Prime Numbers between 1 to n :

def primeSum(end):

    sum = 0

    for num in range(1, end + 1):

        if num > 1:

            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                sum = sum + num

    return sum


end = int(input("Enter N : "))

result = primeSum(end)
print("Sum of Prime No :", result)