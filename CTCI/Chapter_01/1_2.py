"""
Cracking the coding interview exercise 1.2
Given two strings, write a method to decide if one is a permutation of the other.
"""

# my solution
import collections

def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)

    return c1 == c2

print(isPermutation("shre", "ehsy"))

# authors solution
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    letters = [0 for _ in range(128)]
    for char in str1:
        letters[ord(char)] += 1

    for char in str2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False

    return True

print(checkPermutation("shre", "ehsy"))