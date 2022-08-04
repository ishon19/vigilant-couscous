class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s,e in self.calendar:
            # print(s,e, start, end)
            if s<=start<e or s<end<=e or start<=s<end or start<e<=end:
                return False
        self.calendar.append((start , end))
        return True