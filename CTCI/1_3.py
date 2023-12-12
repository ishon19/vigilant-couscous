"""
Cracking the coding interview exercise 1.3

URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string.

Example:
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""


# my solution
import re


def URLify(url, size):
    # get rid of the white spaces
    return "%20".join(re.split('\W+', url.strip()))


print(URLify("Shreyans  pathak", 20))


# authors solution

def urlify(s, true_length):
    # Convert the string to a list of characters
    char_list = list(s)

    # Count the number of spaces
    space_count = sum(1 for c in char_list[:true_length] if c == ' ')

    # New index for the end of the modified string
    new_index = true_length + space_count * 2 - 1

    # Parse the string in reverse order
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            # Replace spaces
            char_list[new_index] = '0'
            char_list[new_index - 1] = '2'
            char_list[new_index - 2] = '%'
            new_index -= 3
        else:
            # Move characters
            char_list[new_index] = char_list[i]
            new_index -= 1

    return ''.join(char_list[:true_length + space_count * 2])


# Example usage
input_str = "Mr John Smith    "
true_length = 13
result = urlify(input_str, true_length)
print(result)  # Output: Mr%20John%20Smith
