
num = [122,24,36,13,26,39,14,28,42,15,30]

minVal = num[0]
maxVal = 0

for i in num :
  if i > maxVal :
    maxVal = i

for i in num :
  if i < minVal :
      minVal = i


print(minVal)
print(maxVal)


