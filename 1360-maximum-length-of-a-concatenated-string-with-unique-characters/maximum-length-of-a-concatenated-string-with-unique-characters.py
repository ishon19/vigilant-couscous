class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0

        def is_unique(s):
            return len(s) == len(set(s))

        def helper(idx, curr):
            if idx == len(arr) and is_unique(curr):
                self.res = max(self.res, len(curr))
                return
            
            # check if the  whole string  is unique
            possible = arr[idx] + curr
            if(is_unique(possible)):
                self.res = max(self.res, len(possible))
                helper(idx + 1, possible)
            helper(idx + 1, curr)
        
        helper(0, "")
        return self.res