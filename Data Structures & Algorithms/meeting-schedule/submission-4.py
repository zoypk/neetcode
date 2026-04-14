"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        # Since they are sorted, lets comopare the start value of one to the end value of prevEND
        for i in range(1,len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

