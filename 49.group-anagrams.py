#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)

        for word in strs:
            hash = ''.join(sorted(word))
            anagramList[hash].append(word)
        
        return list(anagramList.values())
        
# @lc code=end

