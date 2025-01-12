class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        heapq.heapify(minHeap)
        res = 0

        for i_start, i_end in intervals:
            if len(minHeap) == 0:
                heapq.heappush(minHeap, i_end)
            else:
                curr_end = minHeap[0]
                if curr_end > i_start:
                    heapq.heappush(minHeap, i_end)
                else:
                    heapq.heappushpop(minHeap, i_end)
            res = max(res, len(minHeap))
        
        return res
