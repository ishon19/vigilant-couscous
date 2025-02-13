#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        q = deque([0])
        seen = set()
        wordset = set(wordDict)

        while q:
            start = q.popleft()

            if start == n:
                return True

            for end in range(start + 1, n + 1):
                if end in seen:
                    continue

                if s[start:end] in wordset:
                    q.append(end)
                    seen.add(end)
        
        return False
# @lc code=end

