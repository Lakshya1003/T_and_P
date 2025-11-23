#Create a list of 10 numbers and print the sum of even numbers only.

num = [11,12,33,34,44,45,55,56,66,67]
sum = 0
for i in num :
  if i % 2 == 0 :
    sum = sum + i

print(sum)