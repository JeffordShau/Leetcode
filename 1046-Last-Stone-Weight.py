import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap: store vals * -1
        # interate through stones * -1

        # heapify
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            heavier = heappop(maxHeap)
            lighter = heappop(maxHeap)

            if heavier != lighter:
                heavier = heavier * -1
                lighter = lighter * -1
                print(heavier, lighter)
                difference = heavier - lighter
                heapq.heappush(maxHeap, difference * -1)

        if len(maxHeap) == 0:
            return 0
        else:
            return maxHeap[0] * -1
        