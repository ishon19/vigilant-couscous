class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}

        def helper(steps, clip, pattern):
            # Base cases
            if len(pattern) == n:
                return steps
            if len(pattern) > n or steps > n:
                return float('inf')
            
            # Memoization check
            key = (len(pattern), len(clip))
            if key in memo:
                return memo[key]

            # Recursive calls
            # Option 1: Copy all and paste
            copy_paste = helper(steps + 2, pattern, pattern + pattern)
            # Option 2: Paste clipboard content
            paste = float('inf')
            if clip:
                paste = helper(steps + 1, clip, pattern + clip)

            # Store result in memo and return
            memo[key] = min(copy_paste, paste)
            return memo[key]

        # Start with 0 steps, empty clipboard, and "A" as the initial pattern
        return helper(0, '', 'A')
