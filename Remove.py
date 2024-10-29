'''
Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo
'''
# Step 1: Take a string from the user
user_input = input("Enter a string: ")

# Step 2: Take the index position from the user
index = int(input("Enter the index position to remove: "))

# Step 3: Remove the nth index character
if 0 <= index < len(user_input):
    new_string = user_input[:index] + user_input[index + 1:]  # Slice to remove the character
else:
    new_string = user_input  # If index is out of bounds, return the original string

# Step 4: Print the resulting string
print("Resulting String:", new_string)

# Step 5: Exit (implicit)
