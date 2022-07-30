class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a combined array of positions and speed
        info = [[p,s] for p, s in zip(position, speed)]
        
        # start in the reverse order
        # and compare if the times of two different
        # cars can overlap or not, if they do then 
        # we know they form a fleet
        stack = []
        for p,s in sorted(info)[::-1]:
            time = (target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)