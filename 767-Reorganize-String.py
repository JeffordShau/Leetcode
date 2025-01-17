class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        maxHeap = [(-nums, char) for char, nums in freq.items()]
        heapq.heapify(maxHeap)
        res = []
        prev = (0, '')

        while maxHeap:
            num, char = heapq.heappop(maxHeap)
            res.append(char)
            num += 1
            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            prev = (num, char)

        if len(res) != len(s):
            return ""
            
        return ''.join(res)