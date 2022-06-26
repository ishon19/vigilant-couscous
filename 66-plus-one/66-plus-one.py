class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1 
        
        for i in reversed(range(1, len(digits))):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1
        
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        
        return digits
        