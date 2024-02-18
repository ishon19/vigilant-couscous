class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        q = collections.deque(nums)
        res = []
        while q:
            if len(q) == 1:
                break         
            else:
                score = 0
                for i in range(2):
                    score += q.popleft()
                if res:
                    if res[-1] == score:
                        res.append(score)
                    else:
                        break
                else:
                    res.append(score)
        
        return len(res)