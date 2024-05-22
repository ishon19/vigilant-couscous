class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(res, path, s):
            if not s:
                res.append(path)
                
            for i in range(1, len(s)+1):
                if s[:i]==s[:i][::-1]:
                    helper(res, path+[s[:i]], s[i:])
        
        res = []
        helper(res, [], s)
        return res
            