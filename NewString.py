'''
 Write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string.
Problem Description:
The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize a count variable to 0.
3. Use a for loop to traverse through the characters in the string and increment the count variable each time.
4. Form the new string using string slicing.
5. Print the newly formed string.
6. Exit.
Sample Input:
Hello World
Sample Output:
Held
'''
# Step 1: Take a string from the user
user_input = input("Enter a string: ")

# Step 2: Check the length of the string
length = len(user_input)

# Step 3: Form the new string using string slicing
if length >= 2:
    new_string = user_input[:2] + user_input[-2:]  # First 2 and last 2 characters
else:
    new_string = user_input  # If string is shorter than 2, return as is

# Step 4: Print the newly formed string
print("New String:", new_string)

# Step 5: Exit (implicit)
