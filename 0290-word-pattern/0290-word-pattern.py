class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1 = list(pattern)
        s2 = s.split(" ")
        if len(s1) != len(s2):
            return False
        z = zip(s1, s2)
        c = {}
        
        for k, v in z:
            if k not in c:
                c[k] = v
            else:
                if c[k] != v:
                    return False
        
        if len(set(s2)) != len(set(s1)):
            return False
        
        return True
        
        
        