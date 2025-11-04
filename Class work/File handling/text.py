file = open("result.txt")
file.close()
"""
read() => complete in string
readline() => first line in string
readlines() => complete in list

"""
with open('result.txt','a') as file:
  name = input("Enter name : ")
  clg = input("Enter clg : ")
  enroll = input("Enter enroll : ")
  contact = input("Enter contact : ")
  file.write("\n")
  file.write(f"{name},{clg},{enroll},{contact}\n")
  file.append()
