
#Write a program to insert a value at a given index from user input.

num = [11,12,33,34,44,45,55,56,66,67]

value = int(input("Enter value : "))
index = int(input("Enter index : "))

num.insert(index,value)

print(num)