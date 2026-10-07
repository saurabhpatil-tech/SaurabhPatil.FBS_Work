
# Q3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.


words = ["python", "java", "python", "c", "java", "python" , "Html"]

unique_words = set(words)

for i in unique_words:
    print(i, ":", words.count(i))