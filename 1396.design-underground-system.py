#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        # hashmap to maintain travel information
        # can store (from, to) pairs as key
        # and (customerId, time) to facilitate calculations
        self.travelInfo = defaultdict(list)

        # (customerId -> station, check in/out Time)
        self.checkInInfo = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkInInfo:
            self.checkInInfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkInInfo:
            startStation, startTime = self.checkInInfo[id]
            self.travelInfo[(startStation, stationName)].append(t - startTime)
            del self.checkInInfo[id]
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.travelInfo:
            info = self.travelInfo[(startStation, endStation)]
            return sum(info) / len(info)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

