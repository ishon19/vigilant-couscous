class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): 
            return []
        
        charMap = {'2': 'abc', '3': 'def', '4': 'ghi',
                   '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                   '9': 'wxyz'}
        ans = []
        
        def backtrack(idx, path):
            if (idx == len(digits)):
                ans.append("".join(path))
                return
            
            letters = charMap[digits[idx]]
            for letter in letters:
                path[idx] = letter
                backtrack(idx+1, path)                
        
        backtrack(0, ["0"]*len(digits))
        return ans
        