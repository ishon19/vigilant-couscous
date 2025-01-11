class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        tokens = p.split('*')

        for token in tokens:
            if token != '' and token not in s:
                return False
        
        idx = s.index(tokens[0]) + len(tokens[0])
        print(idx)

        if tokens[0]!='' and tokens[1] not in s[idx:]:
            return False
        elif tokens[0] == '' and tokens[1] not in s:
            return False
        
        return True