class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums: # O(n)
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif num >= minHeap[0]:
                if len(minHeap) == k:
                    heapq.heappushpop(minHeap, num) # O(logk)
                else:
                    heapq.heappush(minHeap, num) # O(logk)
        
        return minHeap[0]

        # O(n logk)
                