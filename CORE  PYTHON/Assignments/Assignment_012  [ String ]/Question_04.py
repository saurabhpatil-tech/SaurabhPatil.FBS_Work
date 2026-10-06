
# Q4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged.

str = input("Enter String:")

First = str[0]
Last = str[-1]
Middle = str[1:-1]

res = Last + Middle + First

print(res)