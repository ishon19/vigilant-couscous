class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))
        
        events.sort()
        
        numPassengers = 0
        for event, change in events:
            numPassengers += change

            if numPassengers > capacity:
                return False 

        return True 