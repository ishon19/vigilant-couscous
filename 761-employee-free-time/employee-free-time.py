# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flatlist = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res = []
        end = flatlist[0].end
        for item in flatlist[1:]:
            if item.start>end:
                res.append(Interval(end, item.start))
            end = max(end, item.end)
        return res

        