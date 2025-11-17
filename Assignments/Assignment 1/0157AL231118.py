# ================================================
# Python Assignment: Loops and Conditional Logic
# ================================================

# ================================================
# Section A: Basic Conditional Problems
# ================================================

# === Question 1: Check if a number is positive, negative, or zero ===
print("\n--- Question 1 ---")
input_number = int(input("Input a number: "))
if input_number > 0:
    print(f"The number {input_number} is positive.")
elif input_number < 0:
    print(f"The number {input_number} is negative.")
else:
    print("The number is zero.")

# === Question 2: Check if a number is even or odd ===
print("\n--- Question 2 ---")
num = int(input("Input a number: "))
if num % 2 == 0: # Check if the number is divisible by 2
    print(f"{num} is an even number.") # If remainder is 0, it's even
else:
    print(f"{num} is an odd number.") # Otherwise, it's odd

# === Question 3: Check if a year is a leap year ===
print("\n--- Question 3 ---")
input_year = int(input("Input a year: "))
is_leap_year = False # Initialize leap year flag
if input_year % 4 == 0: # A year divisible by 4 is potentially a leap year
    if input_year % 100 == 0: # Century years
        if input_year % 400 == 0: # Century years divisible by 400 are leap years
            is_leap_year = True
    else: # Non-century years divisible by 4 are leap years
        is_leap_year = True

if is_leap_year:
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")

# === Question 4: Find the greater of two numbers ===
print("\n--- Question 4 ---")
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
if x > y:
    print(f"The greater number is {x}.") # x is greater than y
elif y > x:
    print(f"The greater number is {y}.") # y is greater than x
else:
    print("Both numbers are equal.")

# === Question 5: Check voting eligibility ===
print("\n--- Question 5 ---")
person_age = int(input("Input age: "))
if person_age >= 18: # Check if age is 18 or above
    print("This person is eligible to vote.")
else: # Otherwise, not eligible
    print("This person is not eligible to vote.")

# === Question 6: Check for a vowel or consonant ===
print("\n--- Question 6 ---")
character = input("Input a character: ")
vowel_list = ['a', 'e', 'i', 'o', 'u']
if character.lower() in vowel_list: # Convert to lowercase for case-insensitive check
    print(f"'{character}' is a vowel.")
else: # If not a vowel, it's a consonant
    print(f"'{character}' is a consonant.")

# === Question 7: Check if divisible by 5 ===
print("\n--- Question 7 ---")
num_check = int(input("Input a number: "))
if num_check % 5 == 0:
    print(f"{num_check} is divisible by 5.") # Check for divisibility by 5
else:
    print(f"{num_check} is not divisible by 5.") # Not divisible by 5

# === Question 8: Check number of digits ===
print("\n--- Question 8 ---")
val = int(input("Input a positive number: "))
if 0 <= val <= 9:
    print("It is a single-digit number.")
elif 10 <= val <= 99: # Check for two-digit numbers
    print("It is a two-digit number.")
else: # Numbers with more than two digits
    print("It has more than two digits.")

# === Question 9: Check if passed or failed ===
print("\n--- Question 9 ---")
score = int(input("Input marks: "))
if score >= 40:
    print("Result: Pass") # Marks 40 or above are passing
else:
    print("Result: Fail") # Marks below 40 are failing

# === Question 10: Check if a multiple of 3 and 7 ===
print("\n--- Question 10 ---")
num_val = int(input("Input a number: "))
if num_val % 21 == 0:
    print(f"{num_val} is a multiple of both 3 and 7.")
else: # If not divisible by 21, it's not a multiple of both
    print(f"{num_val} is not a multiple of both 3 and 7.")

# ================================================
# Section B: Advanced Conditional Problems
# ================================================

# === Question 11: Find the greatest among three numbers ===
print("\n--- Question 11 ---")
n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))
n3 = int(input("Input the third number: "))
largest = n1 # Assume n1 is the largest initially
if n2 > largest: # Compare with n2
    largest = n2 # Update if n2 is larger
if n3 > largest: # Compare with n3
    largest = n3 # Update if n3 is larger
print(f"The largest number is {largest}.")

# === Question 12: Classify a person based on age ===
print("\n--- Question 12 ---")
age_val = int(input("Input age: "))
if age_val < 13:
    category = "Child" # Age less than 13
elif age_val <= 19: # Age between 13 and 19 (inclusive)
    category = "Teenager"
elif age_val <= 59: # Age between 20 and 59 (inclusive)
    category = "Adult"
else: # Age 60 or above
    category = "Senior"
print(f"This person is a {category}.")

# === Question 13: Assign grades based on marks ===
print("\n--- Question 13 ---")
marks = int(input("Input marks: "))
grade = ''
if 90 <= marks <= 100: # Marks for Grade A
    grade = "A"
elif 75 <= marks <= 89: # Marks for Grade B
    grade = "B"
elif 50 <= marks <= 74: # Marks for Grade C
    grade = "C"
elif 35 <= marks <= 49: # Marks for Grade D
    grade = "D"
else: # Marks for Fail
    grade = "Fail"
print(f"The grade is: {grade}")

# === Question 14: Check the type of triangle ===
print("\n--- Question 14 ---")
s1 = int(input("Input side 1: "))
s2 = int(input("Input side 2: "))
s3 = int(input("Input side 3: "))
if s1 == s2 and s2 == s3: # All sides are equal
    print("The triangle is Equilateral.")
elif s1 == s2 or s2 == s3 or s1 == s3: # Exactly two sides are equal
    print("The triangle is Isosceles.")
else: # No sides are equal
    print("The triangle is Scalene.")

# === Question 15: Check the type of character ===
print("\n--- Question 15 ---")
inp_char = input("Input a character: ")
if inp_char.islower():
    print("The character is lowercase.")
elif inp_char.isupper(): # Check if uppercase
    print("The character is uppercase.")
elif inp_char.isdigit(): # Check if digit
    print("The character is a digit.")
else: # Otherwise, it's a special symbol
    print("The character is a special symbol.")

# === Question 16: Calculate electricity bill ===
print("\n--- Question 16 ---")
units = int(input("Input units consumed: "))
total_bill = 0
if units <= 100: # First 100 units
    total_bill = units * 5
elif units <= 200: # Next 100 units (101-200)
    total_bill = (100 * 5) + ((units - 100) * 7)
else: # Units above 200
    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Total electricity bill: {total_bill}")

# === Question 17: Find the largest of four numbers ===
print("\n--- Question 17 ---")
val1 = int(input("Input number 1: "))
val2 = int(input("Input number 2: "))
val3 = int(input("Input number 3: "))
val4 = int(input("Input number 4: "))
max_val = val1 # Assume val1 is the maximum
if val2 > max_val: # Compare with val2
    max_val = val2 # Update if val2 is larger
if val3 > max_val: # Compare with val3
    max_val = val3 # Update if val3 is larger
if val4 > max_val: # Compare with val4
    max_val = val4 # Update if val4 is larger
print(f"The largest value is {max_val}.")

# === Question 18: Check for a century leap year ===
print("\n--- Question 18 ---")
check_year = int(input("Input a year: "))
if check_year % 100 == 0:
    if check_year % 400 == 0: # Century years divisible by 400 are leap years
        print("This is a century leap year.")
    else: # Century years not divisible by 400 are not leap years
        print("This is a century year, but not a leap year.")
else: # Not a century year
    print("This is not a century year.")

# === Question 19: Classify BMI value ===
print("\n--- Question 19 ---")
bmi_val = float(input("Input BMI value: "))
if bmi_val < 18.5:
    result = "Underweight" # BMI less than 18.5
elif bmi_val < 25: # BMI between 18.5 and 24.9
    result = "Normal"
elif bmi_val < 30: # BMI between 25 and 29.9
    result = "Overweight"
else: # BMI 30 or greater
    result = "Obese"
print(f"The BMI category is: {result}")

# === Question 20: Find the smallest of three numbers ===
print("\n--- Question 20 ---")
v1 = int(input("Input number 1: "))
v2 = int(input("Input number 2: "))
v3 = int(input("Input number 3: "))
smallest = v1 # Assume v1 is the smallest initially
if v2 < smallest: # Compare with v2
    smallest = v2 # Update if v2 is smaller
if v3 < smallest: # Compare with v3
    smallest = v3 # Update if v3 is smaller
print(f"The smallest value is {smallest}.")

# ================================================
# Section C: For Loop Problems
# ================================================

# === Question 21: Find Armstrong numbers between 100 and 999 ===
print("\n--- Question 21 ---")
for num_iter in range(100, 1000):
    sum_of_cubes = 0 # Initialize sum of cubes of digits
    temporary_number = num_iter
    while temporary_number > 0:
        digit = temporary_number % 10 # Get the last digit
        sum_of_cubes += digit ** 3 # Add the cube of the digit to the sum
        temporary_number //= 10 # Remove the last digit
    if num_iter == sum_of_cubes: # Check if it's an Armstrong number
        print(num_iter)

# === Question 22: Generate the first n prime numbers ===
print("\n--- Question 22 ---")
limit = int(input("How many prime numbers to generate?: "))
primes_found = 0
current_number = 2
while primes_found < limit:
    is_prime_candidate = True # Assume current_number is prime
    for i in range(2, int(current_number**0.5) + 1): # Check for divisors up to the square root
        if current_number % i == 0: # If divisible, it's not prime
            is_prime_candidate = False
            break
    if is_prime_candidate: # If no divisors found, it's prime
        print(current_number)
        primes_found += 1
    current_number += 1 # Move to the next number

# === Question 23: Numbers from 1 to 500 divisible by 3 with digit sum <= 10 ===
print("\n--- Question 23 ---")
for i in range(1, 501):
    if i % 3 == 0:
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum <= 10: # Check if the sum of digits is 10 or less
            print(i)

# === Question 24: Print a pyramid of stars ===
print("\n--- Question 24 ---")
height = int(input("Input pyramid height: "))
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1)) # Print spaces then stars

# === Question 25: Check if a string is a pangram ===
print("\n--- Question 25 ---")
text = input("Input a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
found_letters = set()
for char in text.lower(): # Iterate through the input text
    if char in alphabet: # Check if the character is an alphabet letter
        found_letters.add(char) # Add unique letters to the set
if len(found_letters) == 26: # A pangram contains all 26 letters
    print("The text is a pangram.")
else:
    print("The text is not a pangram.")

# === Question 26: Find twin primes between 1 and 100 ===
print("\n--- Question 26 ---")
prime_list = []
for number_candidate in range(2, 101):
    is_prime = True # Assume the number is prime
    for i in range(2, int(number_candidate**0.5) + 1): # Check for divisors
        if number_candidate % i == 0: # If divisible, not prime
            is_prime = False
            break
    if is_prime:
        prime_list.append(number_candidate) # Add to list if prime

for i in range(len(prime_list) - 1): # Iterate through the list of primes
    if prime_list[i+1] - prime_list[i] == 2: # Check if the difference is 2
        print(f"({prime_list[i]}, {prime_list[i+1]})")

# === Question 27: Check for a Harshad number ===
print("\n--- Question 27 ---")
num_input_str = input("Input a number: ")
num_val = int(num_input_str)
sum_of_digits_val = 0 # Initialize sum of digits
for digit_char in num_input_str: # Iterate through each character in the string
    sum_of_digits_val += int(digit_char) # Convert char to int and add to sum
if num_val > 0 and num_val % sum_of_digits_val == 0: # Check Harshad condition
    print("This is a Harshad Number.")
else:
    print("This is not a Harshad Number.")

# === Question 28: Generate Pascal's Triangle ===
print("\n--- Question 28 ---")
rows = int(input("Input number of rows: "))
current_row = [1]
for i in range(rows): # Loop for each row
    print(" ".join(map(str, current_row))) # Print the current row
    next_row = [1] # Start next row with 1
    for j in range(len(current_row) - 1): # Calculate intermediate values
        next_row.append(current_row[j] + current_row[j+1]) # Sum of two numbers above
    next_row.append(1) # End next row with 1
    current_row = next_row # Update current_row for the next iteration

# === Question 29: Calculate the sum of squares series ===
print("\n--- Question 29 ---")
n_limit = int(input("Input the value of n: "))
total_sum = 0
for i in range(1, n_limit + 1):
    total_sum += i * i # Add the square of each number
print(f"The sum is: {total_sum}")

# === Question 30: Check for a Strong number ===
print("\n--- Question 30 ---")
facts = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
num_str = input("Input a number: ")
fact_sum = 0
for digit_char in num_str: # Iterate through each digit character
    fact_sum += facts[digit_char] # Add factorial of the digit
if fact_sum == int(num_str): # Check if sum of factorials equals the number
    print("This is a Strong Number.")
else:
    print("This is not a Strong Number.")

# ================================================
# Section D: While Loop Problems
# ================================================

# === Question 31: Reverse a number and check if the reverse is prime ===
print("\n--- Question 31 ---")
original_num = int(input("Input a number: "))
reversed_number = 0 # Initialize reversed number
temporary_number = original_num
while temporary_number > 0:
    reversed_number = (reversed_number * 10) + (temporary_number % 10) # Build reversed number
    temporary_number //= 10 # Remove last digit

is_prime_reversed = True # Assume reversed number is prime
if reversed_number < 2: # Numbers less than 2 are not prime
    is_prime_reversed = False
else:
    divisor_check = 2
    while divisor_check * divisor_check <= reversed_number: # Check for divisors up to square root
        if reversed_number % divisor_check == 0: # If divisible, not prime
            is_prime_reversed = False
            break
        divisor_check += 1 # Move to next potential divisor
if is_prime_reversed:
    print(f"The reversed number {reversed_number} is prime.")
else:
    print(f"The reversed number {reversed_number} is not prime.")

# === Question 32: Accept numbers until the sum of their digits exceeds 100 ===
print("\n--- Question 32 ---")
master_sum = 0
while master_sum <= 100:
    print(f"Current sum of all digits: {master_sum}")
    input_string = input("Input a number: ")
    current_digit_sum = sum(int(digit) for digit in input_string) # Calculate sum of digits for current input
    master_sum += current_digit_sum # Add to the running total
print(f"The final sum {master_sum} has exceeded 100.")

# === Question 33: Check for a Duck number ===
print("\n--- Question 33 ---")
num_as_str = input("Input a number: ")
if num_as_str[0] != '0' and '0' in num_as_str:
    print("This is a Duck Number.")
else: # Does not meet Duck number criteria
    print("This is not a Duck Number.")

# === Question 34: Check for a Happy number ===
print("\n--- Question 34 ---")
num = int(input("Input a number: "))
history = set()
while num != 1 and num not in history: # Loop until 1 or a cycle is detected
    history.add(num) # Add current number to history
    num = sum(int(digit)**2 for digit in str(num)) # Calculate sum of squares of digits
if num == 1: # If the process ends in 1, it's a Happy Number
    print("This is a Happy Number.")
else:
    print("This is not a Happy Number.")

# === Question 35: Find the largest prime factor of a number ===
print("\n--- Question 35 ---")
num = int(input("Input a number: "))
largest_factor = -1
divisor_candidate = 2
current_value = num
while divisor_candidate * divisor_candidate <= current_value: # Check divisors up to square root
    while current_value % divisor_candidate == 0: # While divisible by current divisor
        largest_factor = divisor_candidate # Update largest prime factor
        current_value //= divisor_candidate # Divide current_value by the divisor
    divisor_candidate += 1 # Move to the next potential divisor
if current_value > 1: # If current_value is still greater than 1, it's the largest prime factor
    largest_factor = current_value
print(f"The largest prime factor is: {largest_factor}")

# === Question 36: Repeatedly accept a string until it is a palindrome ===
print("\n--- Question 36 ---")
while True:
    text_input = input("Input a string: ")
    reversed_text = "".join(reversed(text_input)) # Reverse the input string
    if text_input == reversed_text: # Check if the string is a palindrome
        print("Palindrome detected. Exiting loop.")
        break

# === Question 37: Find the digital root of a number ===
print("\n--- Question 37 ---")
num = int(input("Input a number: "))
while num >= 10:
    num = sum(int(digit) for digit in str(num)) # Sum the digits
print(f"The digital root is: {num}")

# === Question 38: Generate the Collatz sequence ===
print("\n--- Question 38 ---")
n = int(input("Input a number: "))
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0: # If n is even
        n //= 2 # Divide by 2
    else: # If n is odd
        n = 3 * n + 1 # Multiply by 3 and add 1
print(1)

# === Question 39: Check for a Kaprekar number ===
print("\n--- Question 39 ---")
k_num = int(input("Input a number: "))
square_str = str(k_num**2)
is_kaprekar = False
part1_str = square_str[:i]
part2_str = square_str[i:]
if part1_str and part2_str:
    part1 = int(part1_str)
    part2 = int(part2_str)
    if part1 > 0 and part2 > 0 and part1 + part2 == k_num:
        is_kaprekar = True
if is_kaprekar:
    print("This is a Kaprekar Number.")
else:
    print("This is not a Kaprekar Number.")

# === Question 40: Simulate an ATM machine ===
print("\n--- Question 40 ---")
balance = 1000
while True:
    print("\n-- ATM --")
    print("1. View Balance")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Quit")
    choice = int(input("Select an option: "))
    if choice == 1:
        print(f"Your current balance is: {balance}")
    elif choice == 2:
        deposit_amt = int(input("Enter deposit amount: "))
        balance += deposit_amt
    elif choice == 3:
        withdraw_amt = int(input("Enter withdrawal amount: "))
        if withdraw_amt <= balance:
            balance -= withdraw_amt
        else:
            print("Action failed: Insufficient funds.")
    elif choice == 4:
        break
    else:
        print("Invalid option selected.")


