# Q11. WAP to check if a given number is Armstrong Number or not. 
# for each task create seperate functions .

def countDigits(num):
    return len(str(num))

def armstrong(num , count):
    temp = num
    sum = 0

    while (temp > 0): 
        d = temp % 10
        sum = sum + (d**count)
        temp = temp // 10

    return sum

def checkArmstrong(num):
    count = countDigits(num)
    sum = armstrong(num , count)

    if sum == num:
        print(f"{num} is Armstrong Number")
    else:
        print(f"{num} is Not Armstrong Number")


num = int(input("Enter Number :"))
checkArmstrong(num)


