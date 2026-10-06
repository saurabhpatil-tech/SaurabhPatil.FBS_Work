
# Q5. Accept a number from user and Check if this element is present in the list or not. 
# Also tell how many times it is present in the list.


li = [22, 45, 90, 33, 22, 100, 70, 22]

num = int(input("Enter Number:"))

count = 0 

if num in li:
    print(f"{num} is Prsent in List")

    for i in range(len(li)):
        if li[i] == num:
            count += 1

    print("Number of times present :",count)

else:
    print("Element is not present")
