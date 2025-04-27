class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            current = left * left + right * right

            if current == c:
                return True
            elif current < c:
                left += 1
            else:
                right -= 1
        
        return False