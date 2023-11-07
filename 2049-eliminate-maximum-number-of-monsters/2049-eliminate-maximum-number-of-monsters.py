class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivalTime = [dist[i]/speed[i] for i in range(len(dist))]
        arrivalTime.sort()
        ans = 0
        for i in range(len(arrivalTime)):
            if arrivalTime[i] <= i:
                break
            else:
                ans += 1
        return ans