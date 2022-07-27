class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        idxQ = deque()
        
        # loop on the nums list
        for i,n in enumerate(nums):           
            # while the currently added element is greater than the last element
            # keep on popping the smaller ones as we do not need them           
            while idxQ and n>nums[idxQ[-1]]:
                idxQ.pop()
            
            # append the number either way
            idxQ.append(i)
            
            # while the window size is larger than k pop
            # that is we are moving the window 
            while i+1-idxQ[0]>k:
                idxQ.popleft()
            
            if i+1>=k:
                res.append(nums[idxQ[0]])
            
        return res