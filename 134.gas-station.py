#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # key observations
        # - gas should never go negative
        # - total cost to cover should never be less than total gas available
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                current_tank = 0
                start = i + 1

        return start if total_tank >= 0 else -1 

# @lc code=end

