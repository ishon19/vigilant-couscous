class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = defaultdict(int)
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res