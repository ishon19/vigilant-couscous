#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is to group the strings something unique, we can use the
        # sorted version of the strings to create the key
        cache = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in cache:
                cache[sortedWord].append(word)
            else:
                cache[sortedWord] = [word]
        
        return [val for val in cache.values()]

        
# @lc code=end

