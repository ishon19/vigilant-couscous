"""
10 -> 1010 -> 1+1+1
7 ->  0111

3 -> 011 
4 -> 100 -> 1+1+1

4//2 = 0
2//2 = 0
1//2= 1
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def get_binary(num):
            res = ""
            while num>0:
                res += str(num % 2)
                num = num // 2
            return res[::-1]
        
        start_bin = get_binary(start)
        goal_bin = get_binary(goal)

        if len(start_bin) < len(goal_bin):
            start_bin = "0"*(len(goal_bin) - len(start_bin)) + start_bin
        elif len(goal_bin) < len(start_bin):
            goal_bin = "0"*(len(start_bin) - len(goal_bin)) + goal_bin
        
        res = 0
        for a, b in zip(start_bin, goal_bin):
            if a != b:
                res += 1
        return res