class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(start_index):
            if start_index == len(s):
                return True
            
            match = False
            for word in wordDict:
                if s[start_index:].startswith(word):
                    match = match or dfs(start_index + len(word))
            return match
        return dfs(0)