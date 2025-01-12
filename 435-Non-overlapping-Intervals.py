class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        
        _, curr_end = intervals[0]
        for i_start, i_end in intervals[1:]:
            # overlapping intervals
            if curr_end > i_start:
                res += 1
                # current interval ends later than next interval
                if curr_end > i_end:
                    # remove current interval
                    curr_end = i_end
            else:
                # non-overlapping intervals
                curr_end = i_end
        
        return res
                