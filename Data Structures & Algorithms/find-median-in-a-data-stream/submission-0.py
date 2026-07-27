class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.maxheap and num > self.maxheap[0]:
            heapq.heappush(self.maxheap, num)
        else:
            heapq.heappush(self.minheap, -1 * num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            val = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
        elif len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1 * val)
        
    def findMedian(self) -> float:
        """
        [1,2,3]
        [1,2,5,6]

        odd
        [1,2,3]
        [2,4,5]
        even
        """
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return (-1 * self.minheap[0])
        else:
            return (self.maxheap[0] + (-1*self.minheap[0])) / 2.0

        
        