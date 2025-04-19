class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hash maps to store character frequencies
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        # Count characters in target string t
        for char in t:
            t_count[char] += 1

        matches = 0  # Track matching characters found
        min_length = len(s) + 1  # Initialize to impossible length
        min_substring = ""

        # Sliding window approach
        left = 0
        for right in range(len(s)):
            # Expand window by including right character
            s_count[s[right]] += 1
            if s_count[s[right]] <= t_count[s[right]]:
                matches += 1

            # Contract window from left if possible
            while s_count[s[left]] > t_count[s[left]]:
                s_count[s[left]] -= 1
                left += 1
                if left == len(s):
                    break

            # Update minimum window if all characters are matched
            if matches == len(t) and right - left + 1 < min_length:
                min_substring = s[left:right+1]
                min_length = right - left + 1

        return min_substring