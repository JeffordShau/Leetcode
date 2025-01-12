class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        usedRooms = 0

        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        endPtr = 0
        startPtr = 0

        while startPtr < len(intervals):
            if starts[startPtr] >= ends[endPtr]:
                usedRooms -= 1
                endPtr += 1
            usedRooms += 1
            startPtr += 1
        
        return usedRooms