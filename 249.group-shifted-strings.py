#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_shift_pattern(s):
            if len(s) == 1:
                return ('single',)
            
            pattern = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i-1])) % 26
                pattern.append(diff)
            return tuple(pattern)
        
        groups = defaultdict(list)
        for s in strings:
            pattern = get_shift_pattern(s)
            groups[pattern].append(s)
        
        return list(groups.values())
# @lc code=end

