class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def decode(index):
            if index in memo:
                return memo[index]
            
            if s[index] == '0':
                return 0
            
            ways = decode(index + 1)

            if index + 1 < len(s):
                if s[index] == '1' or (s[index] == '2' and s[index+1] <= '6'):
                    ways += decode(index + 2)
            
            memo[index] = ways
            return ways
        
        return decode(0)