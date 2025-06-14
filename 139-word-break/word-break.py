class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache 
        def dfs(start):
            if start == len(s):
                return True 
            
            for word in wordDict:
                end = start + len(word)

                if end <= len(s) and s[start:end] == word and dfs(end):
                    return True 
            
            return False 
        
        return dfs(0)
