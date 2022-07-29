class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        
        # brute force
        # for i in range(len(temperatures)):
        #     minVal = float("inf")
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             # print(temperatures[i], temperatures[j])
        #             ans[i] = min(minVal, j - i)
        #             break
        
        stack = [] # contains set of values - value and idx
        
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                val, idx = stack.pop()
                ans[idx] = (i - idx)
            stack.append((t, i))
        return ans