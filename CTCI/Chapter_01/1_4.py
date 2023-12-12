"""
Cracking the Coding Interview v6: Exercise 1.4

Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

# my solution

import re
import collections


def isPalindromePerm(string):
    if not string:
        return False

    # clean the string
    string = "".join(re.split('\W+', string.strip().lower()))
    print(string)

    # map the characters
    counter = collections.Counter(string)
    print(counter)

    # if there is just one key, it a palindrome
    if len(counter.keys()) == 1:
        return True
    else:
        # if all even its a palindrome
        allEven = True
        for k, v in counter.items():
            if v % 2 != 0:
                allEven = False
                break

        if allEven:
            return True

        # if all even but one odd, palindrome
        oddCount = 0
        for k, v in counter.items():
            if v % 2 != 0:
                oddCount += 1

        if oddCount == 1:
            return True

    return False


print(isPalindromePerm("Test coa"))