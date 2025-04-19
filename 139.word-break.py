#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        q = deque([0])
        seen = set()

        while q:
            start = q.popleft()
            if start == len(s):
                return True

            for end in range(start+1, len(s) + 1):
                if end in seen:
                    continue
                
                if s[start:end] in wordSet:
                    q.append(end)
                    seen.add(end)
        
        return False
# @lc code=end

