# Bubble sort
num = [19,18,15,12,11,13,14,17,16,20]

identifier = False

for i in range(len(num)):
  for j in range(len(num) - i - 1):
    if num[j] > num[j+1] :
      num[j] , num[j+1] = num[j+1] , num[j]
      identifier = True

    if not identifier:
      break

print(num)
