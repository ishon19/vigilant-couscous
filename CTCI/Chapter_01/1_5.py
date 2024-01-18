"""
Cracking the Coding Interview v6: Exercise 1.5

One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
"""

import collections

def checkOneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i, j = 0, 0
    foundDifference = False

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if foundDifference:
                return False
            foundDifference = True

            if len(s1) == len(s2):
                i += 1
        else:
            i += 1
        j += 1

    return True
        

print(checkOneAway("", ""))