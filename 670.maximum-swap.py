#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_occ = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            # does a larger digit appear later
            for d in range(9, int(digit), -1):
                if last_occ.get(d, -1) > i:
                    digits[i], digits[last_occ[d]] = digits[last_occ[d]], digits[i]
                    return int(''.join(digits))
        
        return num
# @lc code=end

