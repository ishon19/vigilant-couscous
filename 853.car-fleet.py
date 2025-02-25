#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        infolist = sorted(zip(position, speed), reverse=True)

        for pos, spd in infolist:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

# @lc code=end

