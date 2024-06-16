class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return reduce(lambda x, y: x + abs(y[0] - y[1]), zip(seats, students), 0)