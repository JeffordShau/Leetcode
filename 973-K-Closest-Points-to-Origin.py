class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (-dist, point))
            else:
                heapq.heappush(minHeap, (-dist, point))
        
        return [point for (dist, point) in minHeap]