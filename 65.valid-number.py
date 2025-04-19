#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
# import re 

# class Solution:
#     def isNumber(self, s: str) -> bool:
#         pattern = r'^[+-]?(\d+\.?\d*|\d*\.\d+)([eE][+-]?\d+)?$'
#         return bool(re.compile(pattern).fullmatch(s))         

# FSM Approach 
class Solution:
    def isNumber(self, s: str) -> bool:
        # State definitions:
        # 0: Start / Initial state
        # 1: Saw Sign (+/-) at the beginning
        # 2: Saw Integer Digits (before dot/e)
        # 3: Saw Dot, but no preceding integer digits (e.g., after sign or start)
        # 4: Saw Integer Digits AND then Dot (e.g. after "5.")
        # 5: Saw Fraction Digits (digits after dot)
        # 6: Saw 'e' or 'E'
        # 7: Saw Exponent Sign (+/-)
        # 8: Saw Exponent Digits
        states = [
            # State 0: Start
            {'sign': 1, 'digit': 2, '.': 3},
            # State 1: Saw Sign (+/-)
            {'digit': 2, '.': 3},
            # State 2: Saw Integer Digits
            {'digit': 2, '.': 4, 'e': 6},
            # State 3: Saw Dot (no integer digits before it)
            {'digit': 5}, # Must have digits after starting dot
            # State 4: Saw Integer Digits AND then Dot
            {'digit': 5, 'e': 6}, # Can have digits or 'e' after "5."
            # State 5: Saw Fraction Digits
            {'digit': 5, 'e': 6},
            # State 6: Saw 'e' or 'E'
            {'sign': 7, 'digit': 8},
            # State 7: Saw Exponent Sign (+/-)
            {'digit': 8},
            # State 8: Saw Exponent Digits
            {'digit': 8}
        ]
        
        current_state = 0
        # Handle edge case of empty string
        if not s:
             return False

        for char in s: # Iterate through original string
            if char.isdigit():
                char_type = 'digit'
            elif char in ['+', '-']:
                char_type = 'sign'
            elif char in ['e', 'E']: # Handle both 'e' and 'E'
                char_type = 'e'
            elif char == '.':
                char_type = '.'
            else:
                # Invalid character encountered anywhere
                return False
                
            if char_type not in states[current_state]:
                # Invalid transition for the current state and character type
                return False
                
            current_state = states[current_state][char_type]
            
        # Define the set of valid final states
        # Integer (2), Integer with dot (4), Decimal with fraction (5), Exponent digits (8)
        valid_final_states = {2, 4, 5, 8}
        return current_state in valid_final_states

# @lc code=end

