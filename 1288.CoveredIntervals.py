class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        n = len(intervals)
        res = n
        i=0
        j=1
        while(j<n):
            if intervals[i][1] >= intervals[j][1]:
                j+=1
                res-=1
            else:
                if intervals[i][0] == intervals[j][0]:
                    res -= 1
                i = j
                j+=1
        return res
            