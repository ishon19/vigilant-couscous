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
        pattern = re.compile(r'^[\s]*[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?[\s]*$')
        return bool(pattern.fullmatch(s))