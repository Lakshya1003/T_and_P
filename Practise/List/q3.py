#Remove all occurrences of a given element from a list.

num = [11,12,13,11,12,13,11,12]

value = int(input("Enter value : "))

for i in num :
  if i == value :
    num.remove(i)

print(num)