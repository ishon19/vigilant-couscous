#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        l, r = 0, len(self.store[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if self.store[key][mid][1] == timestamp:
                return self.store[key][mid][0]
            elif self.store[key][mid][1] <= timestamp:
                r = mid - 1
            else:
                res = self.store[key][mid][0]
                l = mid + 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

