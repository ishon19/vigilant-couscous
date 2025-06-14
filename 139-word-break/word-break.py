class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start] 

            if start == len(s):
                return True 
            
            for word in wordDict:
                end = start + len(word)

                if end <= len(s) and s[start:end] == word and dfs(end):
                    memo[start] = True
                    return True 
                
            memo[start] = False
            return False 
        
        return dfs(0)
