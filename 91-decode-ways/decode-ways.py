class Solution:
    def numDecodings(self, s: str) -> int:
       @cache
       def dfs(start):
        if start == len(s):
            return 1
        
        ways = 0
        if s[start] == '0':
            return ways
        ways += dfs(start+1)
        if 10 <= int(s[start:start+2]) <=26:
            ways += dfs(start + 2)
        
        return ways

       return dfs(0)