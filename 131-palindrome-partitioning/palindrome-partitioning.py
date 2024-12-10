class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 30 Nov 2024, 20.58 PM
        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    path.append(s[start:end])
                    dfs(end, path)
                    path.pop()
        dfs(0, [])
        return res                    
        # def helper(res, path, s):
        #     if not s:
        #         res.append(path)
                
        #     for i in range(1, len(s)+1):
        #         if s[:i]==s[:i][::-1]:
        #             helper(res, path+[s[:i]], s[i:])
        
        # res = []
        # helper(res, [], s)
        # return res
            