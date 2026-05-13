class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        n = len(self.small)
        m = len(self.large)
        if m == n:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        while self.small and self.large:
            if -self.small[0] > self.large[0]:
                heapq.heappush(self.small, -heapq.heappop(self.large))
                heapq.heappush(self.large, -heapq.heappop(self.small))
            else:
                break
        

    def findMedian(self) -> float:
        n = len(self.small) + len(self.large)
        if n%2 != 0:
            m = -self.small[0]
        else:
            m = (-self.small[0] + self.large[0])/2
        return m
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()