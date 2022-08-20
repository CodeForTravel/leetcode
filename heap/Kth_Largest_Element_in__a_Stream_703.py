from heapq import heappop
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)