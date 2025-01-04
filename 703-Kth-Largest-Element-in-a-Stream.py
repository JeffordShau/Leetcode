import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.capacity = k
        self.size = 0

        for num in nums:
            heappush(self.heap, num)
            self.size += 1
            if self.size > self.capacity:
                heappop(self.heap)
                self.size -= 1


    def add(self, val: int) -> int:
        heappush(self.heap, val)
        self.size += 1
        if self.size > self.capacity:
            heappop(self.heap)
            self.size -= 1
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)