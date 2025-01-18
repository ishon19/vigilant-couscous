"""

26 24


"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # brute force approach
        # k = len(nums)
        # INF = float("inf")
        # range_list = [0, INF]
        # idx_track = [0] * k
        # while True:
        #     cur_min, cur_max = INF, -INF
        #     # the list which had the min index
        #     min_list_index = 0
        #     for i in range(k):
        #         cur = nums[i][idx_track[i]]
        #         if cur < cur_min:
        #             cur_min = cur
        #             min_list_index = i
        #         if cur > cur_max:
        #             cur_max=cur
        #     if cur_max - cur_min > range_list[1] - range_list[0]:
        #         range_list[0] = cur_min
        #         range_list[1] = cur_max
        #     idx_track[min_list_index] += 1
        #     if idx_track[min_list_index] == len(nums[min_list_index]):
        #         break
        # return range_list
        res_range = [0, float("inf")]
        pq = []
        max_val=float("-inf")

        for i in range(len(nums)):
            heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        while len(pq) == len(nums):
            min_val, row, col = heappop(pq)
            if max_val - min_val < res_range[1] - res_range[0]:
                res_range[0] = min_val
                res_range[1] = max_val
        
            if col + 1 < len(nums[row]):
                heappush(pq, (nums[row][col+1], row, col+1))
                max_val = max(max_val, nums[row][col+1])
                
        return [res_range[0], res_range[1]]




