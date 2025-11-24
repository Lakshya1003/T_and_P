names = ["Lakshya","Himang","Vishal","Naman","Kaushik"]

for i in range(len(names)):
    swapped = False
    for j in range(len(names) - i - 1):
        if len(names[j]) > len(names[j+1]):
            names[j], names[j+1] = names[j+1], names[j]
            swapped = True
    if not swapped:
        break

print(names)
