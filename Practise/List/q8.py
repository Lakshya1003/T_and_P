
l1 = [11,12,13,14,15]
l2 = [13,14,15,16,17]
l3 = []
for i in range(len(l1)):
  for j in range(len(l2)):
    if l1[i] not in l3 :
      l3.append(l1[i])
    if l2[j] not in l3 :
      l3.append(l2[j])

print(l3)