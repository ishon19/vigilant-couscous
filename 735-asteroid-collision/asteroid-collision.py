class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            active = True

            while active and stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue 
                elif stack[-1] == -a:
                    stack.pop()
                active = False 
            
            if active:
                stack.append(a)
        
        return stack