l1 = [11,12,13,14,15,16]
l2 = [11,12,13,14,15,16]

identifier = False
i = 0
if len(l1) == len(l2):
  while i < len(l1):
    if l1[i] == l2[i]:
      identifier = True
    else :
      identifier = False
      break

    i = i + 1
else :
  print("The size of array is not same")


if identifier:
  print("Yes ,the two list are sorted , and have same size")

else :
  print("The lists are not same")
