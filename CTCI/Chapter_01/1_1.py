"""
Cracking the coding interview exercise 
1.1 Implement an algorithm to determine if a string has all unique characters.
"""

# my solution
import collections

def checkIsUnique(str):
    counter = collections.Counter(str)
    for k, v in counter.items():
        if v > 1:
            return False
    return True

print(checkIsUnique("abcde"))

# authors solution
def isUniqueChars(str):
    # assuming ascii char set with 128 characters
    if len(str) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True

print(isUniqueChars("abcde"))