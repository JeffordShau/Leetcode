class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        maxHeap = [(-freq, key) for key, freq in counter.items()]
        heapq.heapify(maxHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res