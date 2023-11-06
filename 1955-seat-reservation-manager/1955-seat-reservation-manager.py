class SeatManager:

    def __init__(self, n: int):
        self.mp = {}
        self.seats = [i for i in range(1,n+1)]
        heapq.heapify(self.seats)
        

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        self.mp[seat] = 1
        return seat

        

    def unreserve(self, seatNumber: int) -> None:
        self.mp.pop(seatNumber)
        heapq.heappush(self.seats,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)