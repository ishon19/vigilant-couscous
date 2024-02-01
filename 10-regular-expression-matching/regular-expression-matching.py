class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # recursive Solution
        def helper(i, j):
            # if we reach to the end of the input string, it matched
            if i == len(s) and j == len(p):
                return True
            
            # if pattern exhausted, not matched
            if j == len(p):
                return False
            
            # if currenly matching
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == "*":
                return helper(i, j + 2) or (match and helper(i + 1, j))
            
            if match:
                # check the next characters
                return helper(i + 1, j + 1)
            
            return False
        
        return helper(0, 0)

