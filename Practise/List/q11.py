num = [11,12,13,14,15,16,17,18,19,20]
print(num)

target = int(input('Enter the rotatory value : '))

rotated = num[target:] + num[:target]

print(rotated)
