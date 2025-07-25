#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        uniqueWords = set(wordDict)

        q = deque([0])
        seen = set()
        
        while q:
            startIndex = q.popleft()
            
            if startIndex == len(s):
                return True 

            for endIndex in range(startIndex+1, len(s)):
                if endIndex not in seen and s[startIndex+1:endIndex+1] in uniqueWords:
                    q.append(endIndex)
                    seen.add(startIndex)
            
        return False
                    
# @lc code=end

