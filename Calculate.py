'''
Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
Sample Input:
Cyfuno
Sample Output:
Words: 1
Letters: 6
'''
# Step 1: Take a string from the user
user_input = input("Enter a string: ")

# Step 2: Count the number of words
word_count = len(user_input.split())

# Step 3: Count the number of characters
character_count = len(user_input)

# Step 4: Print the results
print(f"Words: {word_count}")
print(f"Letters: {character_count}")

# Step 5: Exit (implicit)

