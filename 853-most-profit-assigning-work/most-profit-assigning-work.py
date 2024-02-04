class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = i = best = 0
        tasks = list(zip(difficulty, profit))
        tasks.sort()
        for skill in sorted(worker):
            while i<len(tasks) and skill >= tasks[i][0]:
                best = max(best, tasks[i][1])
                i += 1
            res += best          
        return res