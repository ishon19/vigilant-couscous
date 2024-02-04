class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        memo = {}

        def helper(idx):
            if idx in memo:
                return memo[idx]
            
            if idx>=len(jobs):
                memo[idx] = 0
                return memo[idx]
            
            nextIdx = bisect.bisect_left(jobs, jobs[idx][1], key= lambda x: x[0])
            ans = max(helper(idx + 1), jobs[idx][2] + helper(nextIdx))
            
            memo[idx] = ans
            return memo[idx]
        
        return helper(0)
            
