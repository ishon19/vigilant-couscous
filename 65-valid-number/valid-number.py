"""
We can write an regex for this problem.
The string 
 - starts with an optional leading and could end with trailing whitespaces
 - can have a sign positive or negative
 - after the sign, some numbers for sure followed by a decimal sign, which is followed by more numbers
 - then comes the `e` sign which can again be followed by a positive or negative sign and some numbers
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        seen_e = False
        seen_digit = False 
        seen_dot = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False 
                if i == len(s) - 1:
                    return False 
            elif char == '.':
                if seen_e or seen_dot:
                    return False 
                seen_dot = True
            elif char in 'eE':
                if seen_e or not seen_digit:
                    return False 
                seen_e = True
                seen_digit = False 
            else:
                return False 
        
        return seen_digit 