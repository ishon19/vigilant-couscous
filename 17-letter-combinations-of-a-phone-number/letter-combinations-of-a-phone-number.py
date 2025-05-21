class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res
            
        charMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if len(digits) == 1:
            return list(charMap[digits[0]])
        
        for char in charMap[digits[0]]:
            for substr in self.letterCombinations(digits[1:]):
                res.append(char + substr)
        
        return res