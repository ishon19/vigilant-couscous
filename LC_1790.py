class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif sorted(s1) != sorted(s2):
            return False
        
        s1 = list(s1)
        s2 = list(s2)
        left, right = 0, len(s1) - 1
 
        while left<=right:
            if s1[left] == s2[left]:
                left += 1
            if s1[right] == s2[right]:
                right -= 1
            if s1[left] != s2[left] and s1[right] != s2[right]:
                s1[left], s1[right] = s1[right], s1[left]
                if s1 == s2:
                    return True
                else:
                    s1[right], s1[left] = s1[left], s1[right]
                    left += 1
                    right -= 1
        return s1 == s2
    
    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]


if __name__ == "__main__":
    s = Solution()
    print(s.areAlmostEqual("abcd", "dcba"))