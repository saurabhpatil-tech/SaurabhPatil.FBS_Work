
# Q3. Python Program to Check if a Given Key Exists in a Dictionary or Not.


student = { 'id':101 , 'name':'Saurabh', 'Address':'Mangrul' }

key = input("Enter Key :")

if student.get(key) is not None:
    print("Key Exists")
else:
    print("Key Not Found")



