class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # seenMap = [0] * len(s)

        # for word in dictionary:
        #     if word in s:
        #         sub = s
        #         while True:
        #             idx = sub.find(word)
        #             if idx == -1:
        #                 break
        #             for i in range(idx, idx + len(word)):
        #                 seenMap[i] = 1
        #             sub = sub[idx+len(word):]
        
        # res = 0
        # for val in seenMap:
        #     if val == 0:
        #         res += 1
        
        # return res

        # the dynamic way
        n, dset = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            
            # we are discarding this letter and
            # moving on to the next one so adding 1 to ans
            ans = dp(start + 1) + 1

            for end in range(start, n):
                curStr = s[start:end+1]
                if curStr in dset:
                    ans = min(ans, dp(end + 1))
            return ans
        
        return dp(0)