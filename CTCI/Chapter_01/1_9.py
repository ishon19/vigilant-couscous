"""
CTCI 1.9: String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g. "waterbottle" is a rotation of "erbottlewat").

Example:
Input:
"waterbottle", "erbottlewat"

Output:
True
"""

def is_substring(s1, s2):
    return s1 in s2

def string_rotation(s1, s2):
    """
    Time: O(N)
    Space: O(N)
    """
    if len(s1) != len(s2):
        return False
    
    return is_substring(s1, s2 + s2)