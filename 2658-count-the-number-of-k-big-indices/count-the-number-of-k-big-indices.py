class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # brute force approach
        # count_left = [0] * len(nums) 
        # count_right = [0] * len(nums)

        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     count_right[i] = count
        
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     count_left[i] = count
        
        # # print(count_left, count_right)
        # res = 0
        # for l, r in zip(count_left, count_right):
        #     if l>=k and r>=k: res += 1
        # return res

        # heap approach
        candidates = [False] * len(nums)
        heap = []

        for i, num in enumerate(nums):
            if len(heap) == k and -heap[0] < num:
                candidates[i] = True
            
            heapq.heappush(heap, -num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        # print('candidates', candidates)
        res = 0

        heap = []
        for i, num in reversed(list(enumerate(nums))):
            if len(heap) == k and -heap[0] < num and candidates[i]:
                res += 1
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)

        return res