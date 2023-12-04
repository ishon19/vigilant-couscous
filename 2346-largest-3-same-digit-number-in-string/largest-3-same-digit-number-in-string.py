class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 2
        possible = []

        while r<len(num):
            if len(set(num[l:r+1])) == 1:
                possible.append(num[l:r+1])
            l += 1
            r += 1
        
        if not possible: return ""

        ans = possible[0]
        for sub in possible[1:]:
            if int(sub) > int(ans):
                ans = sub
        return ans