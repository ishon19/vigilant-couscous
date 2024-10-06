class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = sum(skill)
        n = len(skill)
        req = total // (n // 2)
        pairs = []
        cur = 0

        l, r = 0, len(skill)-1

        while l <= r:
            if skill[l] + skill[r] == req:
                pairs.append([skill[l], skill[r]])
                cur += skill[l] + skill[r]
                l += 1
                r -= 1
            elif skill[l] + skill[r] > req:
                r -= 1
            else:
                l += 1
        
        if len(pairs) != n//2 or cur != total:
            return -1
        
        res = 0
        for a, b in pairs:
            res += a * b

        return res

