#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n

        for log in logs:
            func_id, event, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)

            if event == "start":
                if stack:
                    prev_id, prev_timestamp = stack[-1]
                    res[prev_id] += timestamp - prev_timestamp
                stack.append([func_id, timestamp])
            else:
                curr_id, curr_timestamp = stack.pop()
                res[curr_id] += timestamp - curr_timestamp + 1

                if stack:
                    stack[-1][-1] = timestamp + 1

        return res
# @lc code=end

