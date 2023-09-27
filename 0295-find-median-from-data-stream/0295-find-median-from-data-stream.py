import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.small = 0
        self.large = 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-1*num)
        self.small += 1
        if self.large != 0 and num > self.minHeap[0]:
            heapq.heappush(self.minHeap,num)
            heapq.heappop(self.maxHeap)
            self.large += 1
            self.small -= 1
        if abs(self.small-self.large) > 1:
            if self.small > self.large:
                ele = heapq.heappop(self.maxHeap)
                ele = -1*ele
                heapq.heappush(self.minHeap,ele)
                self.small -= 1
                self.large += 1
            else:
                ele = heapq.heappop(self.minHeap)
                ele = -1*ele
                heapq.heappush(self.maxHeap,ele)
                self.small += 1
                self.large -= 1
         
                


        

    def findMedian(self) -> float:
        if self.small == self.large:
            first = -1*self.maxHeap[0]
            second = self.minHeap[0]
            ans = (first+second)/2
        elif self.small > self.large:
            ans = -1*self.maxHeap[0]
            ans = ans/1
        else:
            ans = self.minHeap[0]
            ans = ans/1
        return ans
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()