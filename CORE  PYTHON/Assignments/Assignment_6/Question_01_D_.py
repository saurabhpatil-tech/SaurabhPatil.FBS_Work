# Q1. Write a program print following patterns :

#  d :-->

for i in range (1,6):

    ch = 65

    for j in range (1,i+1):

        print(chr(ch),end=" ")
        ch += 1

    print()
