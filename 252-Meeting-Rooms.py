class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort()
        _, curr_end = intervals[0]
        for i_start, i_end in intervals[1:]:
            if curr_end > i_start:
                return False
            curr_end = i_end

        return True