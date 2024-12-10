class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # feasibility check
        counts = [0] * 3

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        for i in range(3):
            if counts[i] < k:
                return -1
        
        # sliding window
        window = [0] * 3
        l, res = 0, 0

        for r in range(len(s)):
            window[ord(s[r]) - ord("a")] += 1
            while l <= r and (counts[0]- window[0] < k or counts[1] - window[1] < k or counts[2] - window[2] < k):
                window[ord(s[l]) - ord('a')] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return len(s) - res

