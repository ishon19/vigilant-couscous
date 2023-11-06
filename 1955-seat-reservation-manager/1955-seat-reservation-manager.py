class SeatManager:

    def __init__(self, n: int):
        self.seatCount = n
        self.reservations = [0] * n
        self.vacancies = []
        self.nextAvailable = 0
        

    def reserve(self) -> int:
        idx = self.nextAvailable
        if self.vacancies and self.vacancies[-1] < idx:
            self.reservations[self.vacancies[-1]] = 1
            idx = self.vacancies[-1]
            self.vacancies.pop()
            return idx + 1
        self.reservations[idx] = 1
        self.nextAvailable += 1
        return idx + 1

    def unreserve(self, seatNumber: int) -> None:
        self.reservations[seatNumber - 1] = 0
        self.vacancies.append(seatNumber - 1)
        self.vacancies.sort(reverse=True)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)