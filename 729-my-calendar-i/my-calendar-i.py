class MyCalendar:

    def __init__(self):
        self.events = []
    
    def isFeasible(self, start: int, end: int) -> int:
        l, r, idx = 0, len(self.events)-1, len(self.events)

        while l<=r:
            mid = (l+r)//2
            if self.events[mid][0] > start:
                idx = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return idx

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.isFeasible(startTime, endTime)
        # check if we can insert or not
        if (idx>0 and self.events[idx-1][1]>startTime) or (idx < len(self.events) and self.events[idx][0]<endTime):
            return False
        self.events.insert(idx, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)