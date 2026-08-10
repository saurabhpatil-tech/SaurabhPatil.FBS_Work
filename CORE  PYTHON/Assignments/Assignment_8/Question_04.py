# Q4. Sum of all odd numbers  between 1 to n :

def sumOdd(n):

    sum = 0 
    for i in range (1,n+1):

        if ( i%2 != 0 ):
            sum+=i
            
    return sum

n = int(input("Enter Number :"))

result = sumOdd(n)
print("Sum of All Odd Number :",result)
