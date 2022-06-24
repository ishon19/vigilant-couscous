class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point_counter = defaultdict(int)
        print(point_counter)
        max_element = 0
        for num in nums:
            point_counter[num] += num
            max_element = max(max_element, num)
        print(point_counter)
        dp = [0] * (max_element+1)
        print(point_counter[2])
        dp[1] = point_counter[1]
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + point_counter[i])
        
        return dp[max_element]    
        