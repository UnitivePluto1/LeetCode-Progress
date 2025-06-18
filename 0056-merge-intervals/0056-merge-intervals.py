class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []  
        
        intervals.sort()

        prev = intervals[0]

        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(prev[1], i[1])
            else:
                final.append(prev)
                prev = i
        final.append(prev)
        return final
