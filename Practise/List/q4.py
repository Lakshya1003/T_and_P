#Reverse a list without using reverse() or slicing.

num = [1,2,3,4,5,6,7,8,9,10]

size = len(num)

for i in range(size // 2):
  temp = num[i]
  num[i] = num[size - i - 1]
  num[size - i - 1] = temp

print(num)