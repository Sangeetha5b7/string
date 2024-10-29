'''
Write a Python Program to calculate the number of digits and letters in a string.

Problem Description:
The program takes a string and calculates the number of digits and letters in a string.

Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a digit is encountered and increment the second count variable each time a character is encountered.
4. Print the total count of both the variables.
5. Exit.

Input & Output Format:
Input consists of a string
Output consists of two integers.
First output refers to the total count of the characters.
Second output refers to the total count of the digits.

Sample Input:
Cyfuno2020

Sample Output:
Characters: 6
Digits: 4
'''
# Step 1: Take a string from the user
user_input = input("Enter a string: ")

# Step 2: Initialize count variables to 0
letter_count = 0
digit_count = 0

# Step 3: Use a for loop to traverse through the characters in the string
for char in user_input:
    if char.isdigit():
        digit_count += 1  # Increment digit count
    elif char.isalpha():
        letter_count += 1  # Increment letter count

# Step 4: Print the total count of both variables
print(f"Characters: {letter_count}")
print(f"Digits: {digit_count}")

# Step 5: Exit (implicit)
