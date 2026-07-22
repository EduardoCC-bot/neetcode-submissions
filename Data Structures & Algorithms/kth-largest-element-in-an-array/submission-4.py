class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        heapq.heapify(maxheap)
        i = 0
        res = 0
        for i in range(len(nums)):
            heapq.heappush(maxheap, nums[i])
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return maxheap[0]
